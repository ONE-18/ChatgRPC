# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\"\x06\n\x04Nada\"0\n\x0b\x43hatMessage\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2U\n\nChatServer\x12#\n\nChatStream\x12\x05.Nada\x1a\x0c.ChatMessage0\x01\x12\"\n\x0bSendMessage\x12\x0c.ChatMessage\x1a\x05.Nadab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_NADA']._serialized_start=14
  _globals['_NADA']._serialized_end=20
  _globals['_CHATMESSAGE']._serialized_start=22
  _globals['_CHATMESSAGE']._serialized_end=70
  _globals['_CHATSERVER']._serialized_start=72
  _globals['_CHATSERVER']._serialized_end=157
# @@protoc_insertion_point(module_scope)