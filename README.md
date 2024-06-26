# gRPC

## 简介
- 基于 HTTP2 之上的二进制协议（Protobuf 序列化机制）；
- 一个连接上可以多路复用，并发处理多个请求和响应；
- 多种语言的类库实现；
- 协议缓冲器: 服务定义文件和自动代码生成（.proto 文件和 Protobuf 编译工具）。 
- RPC 还提供了很多扩展点，用于对框架进行功能定制和扩展，例如，通过开放负载均衡接口可以无缝的与第三方组件进行集成对接（Zookeeper、域名解析服务、SLB 服务等）
- 效率高于 restful 服务，编码节约空间，使得在低带宽场景下很有优势
- protobuf通过编译工具生成数据读写代码，提高开发者编码效率。
- 支持向上游传递超时时间，让上游在发现超时时主动决定如何执行后续操作，http1.1则会直接断开连接。

- GRPC是用于微服务间通信的远程过程调用（RPC）框架。gRPC支持四种类型的RPC：

- Unary RPC：客户端发送单个请求并接收单个响应。
- Server streaming RPC（服务器流式）：客户端发送单个请求，作为回报，服务器发送消息流。
- Client streaming RPC（客户端流式）：客户端发送消息流，服务器以单个消息响应。
- Bidirectional streaming RPC（双向流）：在双向流中，客户端和服务器都发送消息流。
- 此外，gRPC unary RPC可以是同步的或异步的。 同步：客户端调用等待服务器响应。 异步：客户端对服务器进行非阻塞调用，服务器异步返回响应。
- 总结：gRPC是一个远程过程调用（RPC）框架，用于微服务间的通信。gRPC支持unary RPC和流式RPC。在gRPC unaryRPC中，客户端发送单个请求并接收单个响应。此外，gRPC中的RPC可以是同步的，也可以是异步的。在同步RPC中，客户端调用等待服务器响应。顾名思义，在异步RPC中，服务器异步返回响应。

## 注册和发现
### consul 
- 服务发现：微服务可注册自己的服务信息，客户端查找微服务信息。
- 健康检查：微服务目前是否可用，防止流量分发到不健康的服务。
- KV store：key value存储。http接口可操作。可存储动态的服务配置，其他元数据。
- 多数据中心：consul实现了raft算法(算法演示：http://thesecretlivesofdata.com/raft/)，支持多数据中心。
- 负载均衡
- 在集群中，每种应用服务都可能不止一个运行实例，订单服务A调用产品服务B，通过ConsulAPI给出的产品服务B可用地址会是多个，同样都是产品服务，有的资源已用90%，有的资源才用10%，为了避免这种资源利用不均匀，如何做到负载均衡呢？

- 常用方式：随机、轮询、最小连接、权重 等。当然，Consul未提供此功能，或用第三方或自己编写实现；

  - 随机方式：实现起来比较简单，在拉取到的应用服务数据列表中，随意挑一个使用就好
  - 轮询方式：需要有个全局变量，记录当前已用到哪个地址了，下标+1的方式取列表中下个健康的地址
  - 最小连接：记录每个应用服务实例当前已产生多少连接，每次使用最小已连接的实例做为本次的连接
  - 权重方式：配置应用服务实例在整体服务中所占的使用比例上限，每次连接后计算更新已连接的占比
### [etcd](https://github.com/etcd-io/etcd)
### `nginx` 也可以做 负载均衡 `grpc_pass` 

## 并发
- 多线程IO密集并发 `futures.ThreadPoolExecutor(max_workers=100)`
- 多进程计算密集并发 1. 使用多进程启动多个端口设置负载均衡 2. 使用多进程启动服务设置同一端口(gprc.so_reuseport 可以绑定同一个端口， 内部设置负载均衡)

## 异常处理
- 客户端
```python
try:
    pass
except grpc.RpcError as e:
    if e.code() == grpc.StatusCode.UNAVAILABLE:
        print("Check your network connection.")
    else:
        print(f"RPC failed: {e.code()} - {e.details()}")
```
- 服务端
```python
try:
    pass
except Exception as e:
    context.set_code(grpc.StatusCode.INTERNAL)
    context.set_details(str(e))
    return pb2.Response()
```
## 超时处理(客户端和服务端)
