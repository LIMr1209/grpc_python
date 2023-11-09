# gRPC

## 简介
- GRPC是用于微服务间通信的远程过程调用（RPC）框架。gRPC支持四种类型的RPC：

- Unary RPC：客户端发送单个请求并接收单个响应。
- Server streaming RPC（服务器流式）：客户端发送单个请求，作为回报，服务器发送消息流。
- Client streaming RPC（客户端流式）：客户端发送消息流，服务器以单个消息响应。
- Bidirectional streaming RPC（双向流）：在双向流中，客户端和服务器都发送消息流。
- 此外，gRPC unary RPC可以是同步的或异步的。 同步：客户端调用等待服务器响应。 异步：客户端对服务器进行非阻塞调用，服务器异步返回响应。
- 总结：gRPC是一个远程过程调用（RPC）框架，用于微服务间的通信。gRPC支持unary RPC和流式RPC。在gRPC unaryRPC中，客户端发送单个请求并接收单个响应。此外，gRPC中的RPC可以是同步的，也可以是异步的。在同步RPC中，客户端调用等待服务器响应。顾名思义，在异步RPC中，服务器异步返回响应。

## 注册和发现


## 负载均衡方案（客户端）


## 并发
- 一个gRPC通道最多可以处理100个并发请求。
