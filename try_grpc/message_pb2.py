# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rmessage.proto\"\x1e\n\x0eWelcomeRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\"\x1f\n\x0cWelcomeReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1b\n\x0b\x44\x61taRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x05\"\x1e\n\x0c\x44\x61taResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\"\x1c\n\tInMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1d\n\nOutMessage\x12\x0f\n\x07message\x18\x01 \x01(\t2\xbc\x01\n\tMessenger\x12+\n\x07Welcome\x12\x0f.WelcomeRequest\x1a\r.WelcomeReply\"\x00\x12-\n\nAddNumbers\x12\x0c.DataRequest\x1a\r.DataResponse\"\x00(\x01\x12,\n\tGetPrimes\x12\x0c.DataRequest\x1a\r.DataResponse\"\x00\x30\x01\x12%\n\x04\x43hat\x12\n.InMessage\x1a\x0b.OutMessage\"\x00(\x01\x30\x01\x62\x06proto3')
)




_WELCOMEREQUEST = _descriptor.Descriptor(
  name='WelcomeRequest',
  full_name='WelcomeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='WelcomeRequest.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=47,
)


_WELCOMEREPLY = _descriptor.Descriptor(
  name='WelcomeReply',
  full_name='WelcomeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='WelcomeReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=80,
)


_DATAREQUEST = _descriptor.Descriptor(
  name='DataRequest',
  full_name='DataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='DataRequest.data', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=109,
)


_DATARESPONSE = _descriptor.Descriptor(
  name='DataResponse',
  full_name='DataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='DataResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=141,
)


_INMESSAGE = _descriptor.Descriptor(
  name='InMessage',
  full_name='InMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='InMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=171,
)


_OUTMESSAGE = _descriptor.Descriptor(
  name='OutMessage',
  full_name='OutMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='OutMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=202,
)

DESCRIPTOR.message_types_by_name['WelcomeRequest'] = _WELCOMEREQUEST
DESCRIPTOR.message_types_by_name['WelcomeReply'] = _WELCOMEREPLY
DESCRIPTOR.message_types_by_name['DataRequest'] = _DATAREQUEST
DESCRIPTOR.message_types_by_name['DataResponse'] = _DATARESPONSE
DESCRIPTOR.message_types_by_name['InMessage'] = _INMESSAGE
DESCRIPTOR.message_types_by_name['OutMessage'] = _OUTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WelcomeRequest = _reflection.GeneratedProtocolMessageType('WelcomeRequest', (_message.Message,), dict(
  DESCRIPTOR = _WELCOMEREQUEST,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:WelcomeRequest)
  ))
_sym_db.RegisterMessage(WelcomeRequest)

WelcomeReply = _reflection.GeneratedProtocolMessageType('WelcomeReply', (_message.Message,), dict(
  DESCRIPTOR = _WELCOMEREPLY,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:WelcomeReply)
  ))
_sym_db.RegisterMessage(WelcomeReply)

DataRequest = _reflection.GeneratedProtocolMessageType('DataRequest', (_message.Message,), dict(
  DESCRIPTOR = _DATAREQUEST,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:DataRequest)
  ))
_sym_db.RegisterMessage(DataRequest)

DataResponse = _reflection.GeneratedProtocolMessageType('DataResponse', (_message.Message,), dict(
  DESCRIPTOR = _DATARESPONSE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:DataResponse)
  ))
_sym_db.RegisterMessage(DataResponse)

InMessage = _reflection.GeneratedProtocolMessageType('InMessage', (_message.Message,), dict(
  DESCRIPTOR = _INMESSAGE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:InMessage)
  ))
_sym_db.RegisterMessage(InMessage)

OutMessage = _reflection.GeneratedProtocolMessageType('OutMessage', (_message.Message,), dict(
  DESCRIPTOR = _OUTMESSAGE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:OutMessage)
  ))
_sym_db.RegisterMessage(OutMessage)



_MESSENGER = _descriptor.ServiceDescriptor(
  name='Messenger',
  full_name='Messenger',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=205,
  serialized_end=393,
  methods=[
  _descriptor.MethodDescriptor(
    name='Welcome',
    full_name='Messenger.Welcome',
    index=0,
    containing_service=None,
    input_type=_WELCOMEREQUEST,
    output_type=_WELCOMEREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddNumbers',
    full_name='Messenger.AddNumbers',
    index=1,
    containing_service=None,
    input_type=_DATAREQUEST,
    output_type=_DATARESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPrimes',
    full_name='Messenger.GetPrimes',
    index=2,
    containing_service=None,
    input_type=_DATAREQUEST,
    output_type=_DATARESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Chat',
    full_name='Messenger.Chat',
    index=3,
    containing_service=None,
    input_type=_INMESSAGE,
    output_type=_OUTMESSAGE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MESSENGER)

DESCRIPTOR.services_by_name['Messenger'] = _MESSENGER

# @@protoc_insertion_point(module_scope)
