# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rprofile.proto\"\x1e\n\x0bUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"$\n\x0bUserProfile\x12\x15\n\rstock_symbols\x18\x01 \x03(\t2>\n\x0eProfileService\x12,\n\x0eGetUserProfile\x12\x0c.UserRequest\x1a\x0c.UserProfileb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'profile_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_USERREQUEST']._serialized_start=17
  _globals['_USERREQUEST']._serialized_end=47
  _globals['_USERPROFILE']._serialized_start=49
  _globals['_USERPROFILE']._serialized_end=85
  _globals['_PROFILESERVICE']._serialized_start=87
  _globals['_PROFILESERVICE']._serialized_end=149
# @@protoc_insertion_point(module_scope)