# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import core_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='peers.proto',
  package='rsctrl.peers',
  serialized_pb='\n\x0bpeers.proto\x12\x0crsctrl.peers\x1a\ncore.proto\"\xa9\x02\n\x0cRequestPeers\x12\x31\n\x03set\x18\x01 \x02(\x0e\x32$.rsctrl.peers.RequestPeers.SetOption\x12\x33\n\x04info\x18\x02 \x02(\x0e\x32%.rsctrl.peers.RequestPeers.InfoOption\x12\x0f\n\x07pgp_ids\x18\x03 \x03(\t\"^\n\tSetOption\x12\t\n\x05OWNID\x10\x01\x12\n\n\x06LISTED\x10\x02\x12\r\n\tCONNECTED\x10\x03\x12\x0b\n\x07\x46RIENDS\x10\x04\x12\t\n\x05VALID\x10\x05\x12\n\n\x06SIGNED\x10\x06\x12\x07\n\x03\x41LL\x10\x07\"@\n\nInfoOption\x12\x0c\n\x08NAMEONLY\x10\x01\x12\t\n\x05\x42\x41SIC\x10\x02\x12\x0c\n\x08LOCATION\x10\x03\x12\x0b\n\x07\x41LLINFO\x10\x04\"[\n\x10ResponsePeerList\x12#\n\x06status\x18\x01 \x02(\x0b\x32\x13.rsctrl.core.Status\x12\"\n\x05peers\x18\x02 \x03(\x0b\x32\x13.rsctrl.core.Person\"\x81\x01\n\x0eRequestAddPeer\x12\x30\n\x03\x63md\x18\x01 \x02(\x0e\x32#.rsctrl.peers.RequestAddPeer.AddCmd\x12\x0e\n\x06pgp_id\x18\x02 \x02(\t\x12\x0e\n\x06ssl_id\x18\x03 \x01(\t\"\x1d\n\x06\x41\x64\x64\x43md\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06REMOVE\x10\x02\"\x93\x01\n\x12RequestExaminePeer\x12\x0e\n\x06pgp_id\x18\x01 \x02(\t\x12\x38\n\x03\x63md\x18\x02 \x02(\x0e\x32+.rsctrl.peers.RequestExaminePeer.ExamineCmd\x12\x0c\n\x04\x63\x65rt\x18\x03 \x02(\t\"%\n\nExamineCmd\x12\n\n\x06IMPORT\x10\x03\x12\x0b\n\x07\x45XAMINE\x10\x04\"\x99\x01\n\x11RequestModifyPeer\x12\x33\n\x03\x63md\x18\x01 \x02(\x0e\x32&.rsctrl.peers.RequestModifyPeer.ModCmd\x12\"\n\x05peers\x18\x02 \x03(\x0b\x32\x13.rsctrl.core.Person\"+\n\x06ModCmd\x12\x08\n\x04NOOP\x10\x00\x12\x0b\n\x07\x41\x44\x44RESS\x10\x01\x12\n\n\x06\x44YNDNS\x10\x02*|\n\rRequestMsgIds\x12\x16\n\x12MsgId_RequestPeers\x10\x01\x12\x18\n\x14MsgId_RequestAddPeer\x10\x02\x12\x1c\n\x18MsgId_RequestExaminePeer\x10\x03\x12\x1b\n\x17MsgId_RequestModifyPeer\x10\x04*,\n\x0eResponseMsgIds\x12\x1a\n\x16MsgId_ResponsePeerList\x10\x01')

_REQUESTMSGIDS = descriptor.EnumDescriptor(
  name='RequestMsgIds',
  full_name='rsctrl.peers.RequestMsgIds',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='MsgId_RequestPeers', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MsgId_RequestAddPeer', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MsgId_RequestExaminePeer', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MsgId_RequestModifyPeer', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=872,
  serialized_end=996,
)


_RESPONSEMSGIDS = descriptor.EnumDescriptor(
  name='ResponseMsgIds',
  full_name='rsctrl.peers.ResponseMsgIds',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='MsgId_ResponsePeerList', index=0, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=998,
  serialized_end=1042,
)


MsgId_RequestPeers = 1
MsgId_RequestAddPeer = 2
MsgId_RequestExaminePeer = 3
MsgId_RequestModifyPeer = 4
MsgId_ResponsePeerList = 1


_REQUESTPEERS_SETOPTION = descriptor.EnumDescriptor(
  name='SetOption',
  full_name='rsctrl.peers.RequestPeers.SetOption',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='OWNID', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='LISTED', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CONNECTED', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FRIENDS', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='VALID', index=4, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SIGNED', index=5, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ALL', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=179,
  serialized_end=273,
)

_REQUESTPEERS_INFOOPTION = descriptor.EnumDescriptor(
  name='InfoOption',
  full_name='rsctrl.peers.RequestPeers.InfoOption',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='NAMEONLY', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='BASIC', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='LOCATION', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ALLINFO', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=275,
  serialized_end=339,
)

_REQUESTADDPEER_ADDCMD = descriptor.EnumDescriptor(
  name='AddCmd',
  full_name='rsctrl.peers.RequestAddPeer.AddCmd',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='ADD', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='REMOVE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=535,
  serialized_end=564,
)

_REQUESTEXAMINEPEER_EXAMINECMD = descriptor.EnumDescriptor(
  name='ExamineCmd',
  full_name='rsctrl.peers.RequestExaminePeer.ExamineCmd',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='IMPORT', index=0, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXAMINE', index=1, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=677,
  serialized_end=714,
)

_REQUESTMODIFYPEER_MODCMD = descriptor.EnumDescriptor(
  name='ModCmd',
  full_name='rsctrl.peers.RequestModifyPeer.ModCmd',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='NOOP', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ADDRESS', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DYNDNS', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=827,
  serialized_end=870,
)


_REQUESTPEERS = descriptor.Descriptor(
  name='RequestPeers',
  full_name='rsctrl.peers.RequestPeers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='set', full_name='rsctrl.peers.RequestPeers.set', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='info', full_name='rsctrl.peers.RequestPeers.info', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pgp_ids', full_name='rsctrl.peers.RequestPeers.pgp_ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTPEERS_SETOPTION,
    _REQUESTPEERS_INFOOPTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=42,
  serialized_end=339,
)


_RESPONSEPEERLIST = descriptor.Descriptor(
  name='ResponsePeerList',
  full_name='rsctrl.peers.ResponsePeerList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='rsctrl.peers.ResponsePeerList.status', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='peers', full_name='rsctrl.peers.ResponsePeerList.peers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=341,
  serialized_end=432,
)


_REQUESTADDPEER = descriptor.Descriptor(
  name='RequestAddPeer',
  full_name='rsctrl.peers.RequestAddPeer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cmd', full_name='rsctrl.peers.RequestAddPeer.cmd', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pgp_id', full_name='rsctrl.peers.RequestAddPeer.pgp_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ssl_id', full_name='rsctrl.peers.RequestAddPeer.ssl_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTADDPEER_ADDCMD,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=435,
  serialized_end=564,
)


_REQUESTEXAMINEPEER = descriptor.Descriptor(
  name='RequestExaminePeer',
  full_name='rsctrl.peers.RequestExaminePeer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pgp_id', full_name='rsctrl.peers.RequestExaminePeer.pgp_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cmd', full_name='rsctrl.peers.RequestExaminePeer.cmd', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cert', full_name='rsctrl.peers.RequestExaminePeer.cert', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTEXAMINEPEER_EXAMINECMD,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=567,
  serialized_end=714,
)


_REQUESTMODIFYPEER = descriptor.Descriptor(
  name='RequestModifyPeer',
  full_name='rsctrl.peers.RequestModifyPeer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cmd', full_name='rsctrl.peers.RequestModifyPeer.cmd', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='peers', full_name='rsctrl.peers.RequestModifyPeer.peers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTMODIFYPEER_MODCMD,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=717,
  serialized_end=870,
)

_REQUESTPEERS.fields_by_name['set'].enum_type = _REQUESTPEERS_SETOPTION
_REQUESTPEERS.fields_by_name['info'].enum_type = _REQUESTPEERS_INFOOPTION
_REQUESTPEERS_SETOPTION.containing_type = _REQUESTPEERS;
_REQUESTPEERS_INFOOPTION.containing_type = _REQUESTPEERS;
_RESPONSEPEERLIST.fields_by_name['status'].message_type = core_pb2._STATUS
_RESPONSEPEERLIST.fields_by_name['peers'].message_type = core_pb2._PERSON
_REQUESTADDPEER.fields_by_name['cmd'].enum_type = _REQUESTADDPEER_ADDCMD
_REQUESTADDPEER_ADDCMD.containing_type = _REQUESTADDPEER;
_REQUESTEXAMINEPEER.fields_by_name['cmd'].enum_type = _REQUESTEXAMINEPEER_EXAMINECMD
_REQUESTEXAMINEPEER_EXAMINECMD.containing_type = _REQUESTEXAMINEPEER;
_REQUESTMODIFYPEER.fields_by_name['cmd'].enum_type = _REQUESTMODIFYPEER_MODCMD
_REQUESTMODIFYPEER.fields_by_name['peers'].message_type = core_pb2._PERSON
_REQUESTMODIFYPEER_MODCMD.containing_type = _REQUESTMODIFYPEER;
DESCRIPTOR.message_types_by_name['RequestPeers'] = _REQUESTPEERS
DESCRIPTOR.message_types_by_name['ResponsePeerList'] = _RESPONSEPEERLIST
DESCRIPTOR.message_types_by_name['RequestAddPeer'] = _REQUESTADDPEER
DESCRIPTOR.message_types_by_name['RequestExaminePeer'] = _REQUESTEXAMINEPEER
DESCRIPTOR.message_types_by_name['RequestModifyPeer'] = _REQUESTMODIFYPEER

class RequestPeers(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUESTPEERS
  
  # @@protoc_insertion_point(class_scope:rsctrl.peers.RequestPeers)

class ResponsePeerList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSEPEERLIST
  
  # @@protoc_insertion_point(class_scope:rsctrl.peers.ResponsePeerList)

class RequestAddPeer(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUESTADDPEER
  
  # @@protoc_insertion_point(class_scope:rsctrl.peers.RequestAddPeer)

class RequestExaminePeer(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUESTEXAMINEPEER
  
  # @@protoc_insertion_point(class_scope:rsctrl.peers.RequestExaminePeer)

class RequestModifyPeer(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUESTMODIFYPEER
  
  # @@protoc_insertion_point(class_scope:rsctrl.peers.RequestModifyPeer)

# @@protoc_insertion_point(module_scope)
