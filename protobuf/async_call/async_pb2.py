# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/async_call/async.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fprotobuf/async_call/async.proto\"\x18\n\x08Requests\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\x17\n\x05Reply\x12\x0e\n\x06result\x18\x01 \x01(\t2\xaf\x01\n\tStreamRpc\x12$\n\x0fGetServerResult\x12\t.Requests\x1a\x06.Reply\x12&\n\x0fGetServerStream\x12\t.Requests\x1a\x06.Reply0\x01\x12\'\n\x10\x43lientSendStream\x12\t.Requests\x1a\x06.Reply(\x01\x12+\n\x12ServerClientStream\x12\t.Requests\x1a\x06.Reply(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf.async_call.async_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUESTS']._serialized_start=35
  _globals['_REQUESTS']._serialized_end=59
  _globals['_REPLY']._serialized_start=61
  _globals['_REPLY']._serialized_end=84
  _globals['_STREAMRPC']._serialized_start=87
  _globals['_STREAMRPC']._serialized_end=262
# @@protoc_insertion_point(module_scope)
