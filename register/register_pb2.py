# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: register.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eregister.proto\"+\n\x0fRegisterRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"1\n\x10RegisterResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t2B\n\x0fRegisterService\x12/\n\x08Register\x12\x10.RegisterRequest\x1a\x11.RegisterResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'register_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_REGISTERREQUEST']._serialized_start=18
  _globals['_REGISTERREQUEST']._serialized_end=61
  _globals['_REGISTERRESPONSE']._serialized_start=63
  _globals['_REGISTERRESPONSE']._serialized_end=112
  _globals['_REGISTERSERVICE']._serialized_start=114
  _globals['_REGISTERSERVICE']._serialized_end=180
# @@protoc_insertion_point(module_scope)