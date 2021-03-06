# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: builder.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='builder.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rbuilder.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"1\n\x0e\x43ontainerImage\x12\x12\n\nrepository\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\"\xa3\x02\n\x07Scripts\x12\x16\n\x0estartup_script\x18\x01 \x01(\t\x12\x1b\n\x13post_startup_script\x18\x02 \x01(\t\x12\x16\n\x0epre_run_script\x18\x03 \x01(\t\x12\x17\n\x0fshutdown_script\x18\x04 \x01(\t\x12\x32\n\x10scripts_behavior\x18\x05 \x01(\x0e\x32\x18.Scripts.ScriptsBehavior\"~\n\x0fScriptsBehavior\x12 \n\x1cSCRIPTS_BEHAVIOR_UNSPECIFIED\x10\x00\x12 \n\x1cSCRIPTS_BEHAVIOR_EVERY_START\x10\x01\x12\'\n#SCRIPTS_BEHAVIOR_AFTER_INSTALLATION\x10\x02\"\x17\n\x07Project\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"\xf3\x01\n\x0b\x45nvironment\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x19\n\x07project\x18\x02 \x01(\x0b\x32\x08.Project\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05owner\x18\x04 \x01(\t\x12\x36\n\x10\x62\x61se_environment\x18\x05 \x01(\x0e\x32\x1c.Environment.BaseEnvironment\x12(\n\x0f\x63ontainer_image\x18\x06 \x01(\x0b\x32\x0f.ContainerImage\x12\x1d\n\rbuild_history\x18\x07 \x03(\x0b\x32\x06.Build\"\x1d\n\x0f\x42\x61seEnvironment\x12\n\n\x06\x44OCKER\x10\x00\"\xa9\x02\n\x05\x42uild\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x1e\n\nbuild_type\x18\x02 \x01(\x0e\x32\n.BuildType\x12\"\n\x0c\x62uild_status\x18\x03 \x01(\x0e\x32\x0c.BuildStatus\x12\x19\n\x11\x62uild_information\x18\x04 \x01(\t\x12\x0c\n\x04sha1\x18\x05 \x01(\t\x12\x14\n\x0clog_location\x18\x06 \x01(\t\x12(\n\x0f\x63ontainer_image\x18\x07 \x01(\x0b\x32\x0f.ContainerImage\x12\x31\n\rcreation_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xaf\x01\n\x0b\x42uildParams\x12\x19\n\x07scripts\x18\x01 \x01(\x0b\x32\x08.Scripts\x12\x35\n\renv_variables\x18\x02 \x03(\x0b\x32\x1e.BuildParams.EnvVariablesEntry\x12\x19\n\x11max_build_timeout\x18\x03 \x01(\x05\x1a\x33\n\x11\x45nvVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"q\n\x17\x42uildEnvironmentRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12!\n\x0b\x65nvironment\x18\x02 \x01(\x0b\x32\x0c.Environment\x12\"\n\x0c\x62uild_params\x18\x03 \x01(\x0b\x32\x0c.BuildParams\"1\n\x18\x42uildEnvironmentResponse\x12\x15\n\x05\x62uild\x18\x01 \x01(\x0b\x32\x06.Build*A\n\tBuildType\x12\x1a\n\x16\x42UILD_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x42UILD_TYPE_CONTAINER\x10\x01*\xb6\x02\n\x0b\x42uildStatus\x12\x1c\n\x18\x42UILD_STATUS_UNSPECIFIED\x10\x00\x12\x17\n\x13\x42UILD_STATUS_QUEUED\x10\x01\x12\x18\n\x14\x42UILD_STATUS_WORKING\x10\x02\x12\x18\n\x14\x42UILD_STATUS_SUCCESS\x10\x03\x12\x18\n\x14\x42UILD_STATUS_FAILURE\x10\x04\x12\x1f\n\x1b\x42UILD_STATUS_INTERNAL_ERROR\x10\x05\x12\x18\n\x14\x42UILD_STATUS_TIMEOUT\x10\x06\x12\x1a\n\x16\x42UILD_STATUS_CANCELLED\x10\x07\x12\x17\n\x13\x42UILD_STATUS_PAUSED\x10\x08\x12\x18\n\x14\x42UILD_STATUS_EXPIRED\x10\t\x12\x18\n\x14\x42UILD_STATUS_PENDING\x10\n2R\n\x07\x42uilder\x12G\n\x10\x42uildEnvironment\x12\x18.BuildEnvironmentRequest\x1a\x19.BuildEnvironmentResponseb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_BUILDTYPE = _descriptor.EnumDescriptor(
  name='BuildType',
  full_name='BuildType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUILD_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUILD_TYPE_CONTAINER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1310,
  serialized_end=1375,
)
_sym_db.RegisterEnumDescriptor(_BUILDTYPE)

BuildType = enum_type_wrapper.EnumTypeWrapper(_BUILDTYPE)
_BUILDSTATUS = _descriptor.EnumDescriptor(
  name='BuildStatus',
  full_name='BuildStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUILD_STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUILD_STATUS_QUEUED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUILD_STATUS_WORKING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUILD_STATUS_SUCCESS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUILD_STATUS_FAILURE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUILD_STATUS_INTERNAL_ERROR', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUILD_STATUS_TIMEOUT', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUILD_STATUS_CANCELLED', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUILD_STATUS_PAUSED', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUILD_STATUS_EXPIRED', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUILD_STATUS_PENDING', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1378,
  serialized_end=1688,
)
_sym_db.RegisterEnumDescriptor(_BUILDSTATUS)

BuildStatus = enum_type_wrapper.EnumTypeWrapper(_BUILDSTATUS)
BUILD_TYPE_UNSPECIFIED = 0
BUILD_TYPE_CONTAINER = 1
BUILD_STATUS_UNSPECIFIED = 0
BUILD_STATUS_QUEUED = 1
BUILD_STATUS_WORKING = 2
BUILD_STATUS_SUCCESS = 3
BUILD_STATUS_FAILURE = 4
BUILD_STATUS_INTERNAL_ERROR = 5
BUILD_STATUS_TIMEOUT = 6
BUILD_STATUS_CANCELLED = 7
BUILD_STATUS_PAUSED = 8
BUILD_STATUS_EXPIRED = 9
BUILD_STATUS_PENDING = 10


_SCRIPTS_SCRIPTSBEHAVIOR = _descriptor.EnumDescriptor(
  name='ScriptsBehavior',
  full_name='Scripts.ScriptsBehavior',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCRIPTS_BEHAVIOR_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCRIPTS_BEHAVIOR_EVERY_START', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCRIPTS_BEHAVIOR_AFTER_INSTALLATION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=267,
  serialized_end=393,
)
_sym_db.RegisterEnumDescriptor(_SCRIPTS_SCRIPTSBEHAVIOR)

_ENVIRONMENT_BASEENVIRONMENT = _descriptor.EnumDescriptor(
  name='BaseEnvironment',
  full_name='Environment.BaseEnvironment',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DOCKER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=635,
  serialized_end=664,
)
_sym_db.RegisterEnumDescriptor(_ENVIRONMENT_BASEENVIRONMENT)


_CONTAINERIMAGE = _descriptor.Descriptor(
  name='ContainerImage',
  full_name='ContainerImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository', full_name='ContainerImage.repository', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag', full_name='ContainerImage.tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=99,
)


_SCRIPTS = _descriptor.Descriptor(
  name='Scripts',
  full_name='Scripts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='startup_script', full_name='Scripts.startup_script', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='post_startup_script', full_name='Scripts.post_startup_script', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pre_run_script', full_name='Scripts.pre_run_script', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shutdown_script', full_name='Scripts.shutdown_script', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scripts_behavior', full_name='Scripts.scripts_behavior', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCRIPTS_SCRIPTSBEHAVIOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=393,
)


_PROJECT = _descriptor.Descriptor(
  name='Project',
  full_name='Project',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='Project.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=418,
)


_ENVIRONMENT = _descriptor.Descriptor(
  name='Environment',
  full_name='Environment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='Environment.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project', full_name='Environment.project', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Environment.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='Environment.owner', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_environment', full_name='Environment.base_environment', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='container_image', full_name='Environment.container_image', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='build_history', full_name='Environment.build_history', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENVIRONMENT_BASEENVIRONMENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=664,
)


_BUILD = _descriptor.Descriptor(
  name='Build',
  full_name='Build',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='Build.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='build_type', full_name='Build.build_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='build_status', full_name='Build.build_status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='build_information', full_name='Build.build_information', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sha1', full_name='Build.sha1', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log_location', full_name='Build.log_location', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='container_image', full_name='Build.container_image', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='Build.creation_time', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='Build.update_time', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=667,
  serialized_end=964,
)


_BUILDPARAMS_ENVVARIABLESENTRY = _descriptor.Descriptor(
  name='EnvVariablesEntry',
  full_name='BuildParams.EnvVariablesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='BuildParams.EnvVariablesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='BuildParams.EnvVariablesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1091,
  serialized_end=1142,
)

_BUILDPARAMS = _descriptor.Descriptor(
  name='BuildParams',
  full_name='BuildParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scripts', full_name='BuildParams.scripts', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='env_variables', full_name='BuildParams.env_variables', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_build_timeout', full_name='BuildParams.max_build_timeout', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BUILDPARAMS_ENVVARIABLESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=967,
  serialized_end=1142,
)


_BUILDENVIRONMENTREQUEST = _descriptor.Descriptor(
  name='BuildEnvironmentRequest',
  full_name='BuildEnvironmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='BuildEnvironmentRequest.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environment', full_name='BuildEnvironmentRequest.environment', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='build_params', full_name='BuildEnvironmentRequest.build_params', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1144,
  serialized_end=1257,
)


_BUILDENVIRONMENTRESPONSE = _descriptor.Descriptor(
  name='BuildEnvironmentResponse',
  full_name='BuildEnvironmentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='build', full_name='BuildEnvironmentResponse.build', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1259,
  serialized_end=1308,
)

_SCRIPTS.fields_by_name['scripts_behavior'].enum_type = _SCRIPTS_SCRIPTSBEHAVIOR
_SCRIPTS_SCRIPTSBEHAVIOR.containing_type = _SCRIPTS
_ENVIRONMENT.fields_by_name['project'].message_type = _PROJECT
_ENVIRONMENT.fields_by_name['base_environment'].enum_type = _ENVIRONMENT_BASEENVIRONMENT
_ENVIRONMENT.fields_by_name['container_image'].message_type = _CONTAINERIMAGE
_ENVIRONMENT.fields_by_name['build_history'].message_type = _BUILD
_ENVIRONMENT_BASEENVIRONMENT.containing_type = _ENVIRONMENT
_BUILD.fields_by_name['build_type'].enum_type = _BUILDTYPE
_BUILD.fields_by_name['build_status'].enum_type = _BUILDSTATUS
_BUILD.fields_by_name['container_image'].message_type = _CONTAINERIMAGE
_BUILD.fields_by_name['creation_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUILD.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUILDPARAMS_ENVVARIABLESENTRY.containing_type = _BUILDPARAMS
_BUILDPARAMS.fields_by_name['scripts'].message_type = _SCRIPTS
_BUILDPARAMS.fields_by_name['env_variables'].message_type = _BUILDPARAMS_ENVVARIABLESENTRY
_BUILDENVIRONMENTREQUEST.fields_by_name['environment'].message_type = _ENVIRONMENT
_BUILDENVIRONMENTREQUEST.fields_by_name['build_params'].message_type = _BUILDPARAMS
_BUILDENVIRONMENTRESPONSE.fields_by_name['build'].message_type = _BUILD
DESCRIPTOR.message_types_by_name['ContainerImage'] = _CONTAINERIMAGE
DESCRIPTOR.message_types_by_name['Scripts'] = _SCRIPTS
DESCRIPTOR.message_types_by_name['Project'] = _PROJECT
DESCRIPTOR.message_types_by_name['Environment'] = _ENVIRONMENT
DESCRIPTOR.message_types_by_name['Build'] = _BUILD
DESCRIPTOR.message_types_by_name['BuildParams'] = _BUILDPARAMS
DESCRIPTOR.message_types_by_name['BuildEnvironmentRequest'] = _BUILDENVIRONMENTREQUEST
DESCRIPTOR.message_types_by_name['BuildEnvironmentResponse'] = _BUILDENVIRONMENTRESPONSE
DESCRIPTOR.enum_types_by_name['BuildType'] = _BUILDTYPE
DESCRIPTOR.enum_types_by_name['BuildStatus'] = _BUILDSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContainerImage = _reflection.GeneratedProtocolMessageType('ContainerImage', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINERIMAGE,
  '__module__' : 'builder_pb2'
  # @@protoc_insertion_point(class_scope:ContainerImage)
  })
_sym_db.RegisterMessage(ContainerImage)

Scripts = _reflection.GeneratedProtocolMessageType('Scripts', (_message.Message,), {
  'DESCRIPTOR' : _SCRIPTS,
  '__module__' : 'builder_pb2'
  # @@protoc_insertion_point(class_scope:Scripts)
  })
_sym_db.RegisterMessage(Scripts)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {
  'DESCRIPTOR' : _PROJECT,
  '__module__' : 'builder_pb2'
  # @@protoc_insertion_point(class_scope:Project)
  })
_sym_db.RegisterMessage(Project)

Environment = _reflection.GeneratedProtocolMessageType('Environment', (_message.Message,), {
  'DESCRIPTOR' : _ENVIRONMENT,
  '__module__' : 'builder_pb2'
  # @@protoc_insertion_point(class_scope:Environment)
  })
_sym_db.RegisterMessage(Environment)

Build = _reflection.GeneratedProtocolMessageType('Build', (_message.Message,), {
  'DESCRIPTOR' : _BUILD,
  '__module__' : 'builder_pb2'
  # @@protoc_insertion_point(class_scope:Build)
  })
_sym_db.RegisterMessage(Build)

BuildParams = _reflection.GeneratedProtocolMessageType('BuildParams', (_message.Message,), {

  'EnvVariablesEntry' : _reflection.GeneratedProtocolMessageType('EnvVariablesEntry', (_message.Message,), {
    'DESCRIPTOR' : _BUILDPARAMS_ENVVARIABLESENTRY,
    '__module__' : 'builder_pb2'
    # @@protoc_insertion_point(class_scope:BuildParams.EnvVariablesEntry)
    })
  ,
  'DESCRIPTOR' : _BUILDPARAMS,
  '__module__' : 'builder_pb2'
  # @@protoc_insertion_point(class_scope:BuildParams)
  })
_sym_db.RegisterMessage(BuildParams)
_sym_db.RegisterMessage(BuildParams.EnvVariablesEntry)

BuildEnvironmentRequest = _reflection.GeneratedProtocolMessageType('BuildEnvironmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUILDENVIRONMENTREQUEST,
  '__module__' : 'builder_pb2'
  # @@protoc_insertion_point(class_scope:BuildEnvironmentRequest)
  })
_sym_db.RegisterMessage(BuildEnvironmentRequest)

BuildEnvironmentResponse = _reflection.GeneratedProtocolMessageType('BuildEnvironmentResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUILDENVIRONMENTRESPONSE,
  '__module__' : 'builder_pb2'
  # @@protoc_insertion_point(class_scope:BuildEnvironmentResponse)
  })
_sym_db.RegisterMessage(BuildEnvironmentResponse)


_BUILDPARAMS_ENVVARIABLESENTRY._options = None

_BUILDER = _descriptor.ServiceDescriptor(
  name='Builder',
  full_name='Builder',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1690,
  serialized_end=1772,
  methods=[
  _descriptor.MethodDescriptor(
    name='BuildEnvironment',
    full_name='Builder.BuildEnvironment',
    index=0,
    containing_service=None,
    input_type=_BUILDENVIRONMENTREQUEST,
    output_type=_BUILDENVIRONMENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BUILDER)

DESCRIPTOR.services_by_name['Builder'] = _BUILDER

# @@protoc_insertion_point(module_scope)
