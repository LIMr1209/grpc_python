# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/unary/unary.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aprotobuf/unary/unary.proto\x12\x05unary\"$\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\"\x1a\n\x08Response\x12\x0e\n\x06result\x18\x01 \x01(\t25\n\x05unary\x12,\n\x07request\x12\x0e.unary.Request\x1a\x0f.unary.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf.unary.unary_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=37
  _globals['_REQUEST']._serialized_end=73
  _globals['_RESPONSE']._serialized_start=75
  _globals['_RESPONSE']._serialized_end=101
  _globals['_UNARY']._serialized_start=103
  _globals['_UNARY']._serialized_end=156
# @@protoc_insertion_point(module_scope)
