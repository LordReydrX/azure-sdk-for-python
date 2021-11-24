# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AddParticipantRequest
    from ._models_py3 import AddParticipantResult
    from ._models_py3 import AddParticipantResultEvent
    from ._models_py3 import AddParticipantWithCallLocatorRequest
    from ._models_py3 import AnswerCallRequest
    from ._models_py3 import AnswerCallResult
    from ._models_py3 import AudioRoutingGroupRequest
    from ._models_py3 import AudioRoutingGroupResult
    from ._models_py3 import CallConnectionProperties
    from ._models_py3 import CallConnectionStateChangedEvent
    from ._models_py3 import CallLocatorModel
    from ._models_py3 import CallParticipant
    from ._models_py3 import CallRecordingProperties
    from ._models_py3 import CallRecordingStateChangeEvent
    from ._models_py3 import CallingOperationResultDetails
    from ._models_py3 import CancelMediaOperationWithCallLocatorRequest
    from ._models_py3 import CancelParticipantMediaOperationRequest
    from ._models_py3 import CancelParticipantMediaOperationWithCallLocatorRequest
    from ._models_py3 import CommunicationError
    from ._models_py3 import CommunicationErrorResponse
    from ._models_py3 import CommunicationIdentifierModel
    from ._models_py3 import CommunicationUserIdentifierModel
    from ._models_py3 import CreateAudioRoutingGroupResult
    from ._models_py3 import CreateCallRequest
    from ._models_py3 import CreateCallResult
    from ._models_py3 import GetAllParticipantsWithCallLocatorRequest
    from ._models_py3 import GetParticipantRequest
    from ._models_py3 import GetParticipantWithCallLocatorRequest
    from ._models_py3 import HoldMeetingAudioRequest
    from ._models_py3 import JoinCallRequest
    from ._models_py3 import JoinCallResult
    from ._models_py3 import MicrosoftTeamsUserIdentifierModel
    from ._models_py3 import MuteParticipantRequest
    from ._models_py3 import ParticipantsUpdatedEvent
    from ._models_py3 import PhoneNumberIdentifierModel
    from ._models_py3 import PlayAudioRequest
    from ._models_py3 import PlayAudioResult
    from ._models_py3 import PlayAudioResultEvent
    from ._models_py3 import PlayAudioToParticipantRequest
    from ._models_py3 import PlayAudioToParticipantWithCallLocatorRequest
    from ._models_py3 import PlayAudioWithCallLocatorRequest
    from ._models_py3 import RedirectCallRequest
    from ._models_py3 import RejectCallRequest
    from ._models_py3 import RemoveParticipantRequest
    from ._models_py3 import RemoveParticipantWithCallLocatorRequest
    from ._models_py3 import ResumeMeetingAudioRequest
    from ._models_py3 import StartCallRecordingResult
    from ._models_py3 import StartCallRecordingWithCallLocatorRequest
    from ._models_py3 import ToneInfo
    from ._models_py3 import ToneReceivedEvent
    from ._models_py3 import TransferCallResult
    from ._models_py3 import TransferCallResultEvent
    from ._models_py3 import TransferToCallRequest
    from ._models_py3 import TransferToParticipantRequest
    from ._models_py3 import UnmuteParticipantRequest
    from ._models_py3 import UpdateAudioRoutingGroupRequest
except (SyntaxError, ImportError):
    from ._models import AddParticipantRequest  # type: ignore
    from ._models import AddParticipantResult  # type: ignore
    from ._models import AddParticipantResultEvent  # type: ignore
    from ._models import AddParticipantWithCallLocatorRequest  # type: ignore
    from ._models import AnswerCallRequest  # type: ignore
    from ._models import AnswerCallResult  # type: ignore
    from ._models import AudioRoutingGroupRequest  # type: ignore
    from ._models import AudioRoutingGroupResult  # type: ignore
    from ._models import CallConnectionProperties  # type: ignore
    from ._models import CallConnectionStateChangedEvent  # type: ignore
    from ._models import CallLocatorModel  # type: ignore
    from ._models import CallParticipant  # type: ignore
    from ._models import CallRecordingProperties  # type: ignore
    from ._models import CallRecordingStateChangeEvent  # type: ignore
    from ._models import CallingOperationResultDetails  # type: ignore
    from ._models import CancelMediaOperationWithCallLocatorRequest  # type: ignore
    from ._models import CancelParticipantMediaOperationRequest  # type: ignore
    from ._models import CancelParticipantMediaOperationWithCallLocatorRequest  # type: ignore
    from ._models import CommunicationError  # type: ignore
    from ._models import CommunicationErrorResponse  # type: ignore
    from ._models import CommunicationIdentifierModel  # type: ignore
    from ._models import CommunicationUserIdentifierModel  # type: ignore
    from ._models import CreateAudioRoutingGroupResult  # type: ignore
    from ._models import CreateCallRequest  # type: ignore
    from ._models import CreateCallResult  # type: ignore
    from ._models import GetAllParticipantsWithCallLocatorRequest  # type: ignore
    from ._models import GetParticipantRequest  # type: ignore
    from ._models import GetParticipantWithCallLocatorRequest  # type: ignore
    from ._models import HoldMeetingAudioRequest  # type: ignore
    from ._models import JoinCallRequest  # type: ignore
    from ._models import JoinCallResult  # type: ignore
    from ._models import MicrosoftTeamsUserIdentifierModel  # type: ignore
    from ._models import MuteParticipantRequest  # type: ignore
    from ._models import ParticipantsUpdatedEvent  # type: ignore
    from ._models import PhoneNumberIdentifierModel  # type: ignore
    from ._models import PlayAudioRequest  # type: ignore
    from ._models import PlayAudioResult  # type: ignore
    from ._models import PlayAudioResultEvent  # type: ignore
    from ._models import PlayAudioToParticipantRequest  # type: ignore
    from ._models import PlayAudioToParticipantWithCallLocatorRequest  # type: ignore
    from ._models import PlayAudioWithCallLocatorRequest  # type: ignore
    from ._models import RedirectCallRequest  # type: ignore
    from ._models import RejectCallRequest  # type: ignore
    from ._models import RemoveParticipantRequest  # type: ignore
    from ._models import RemoveParticipantWithCallLocatorRequest  # type: ignore
    from ._models import ResumeMeetingAudioRequest  # type: ignore
    from ._models import StartCallRecordingResult  # type: ignore
    from ._models import StartCallRecordingWithCallLocatorRequest  # type: ignore
    from ._models import ToneInfo  # type: ignore
    from ._models import ToneReceivedEvent  # type: ignore
    from ._models import TransferCallResult  # type: ignore
    from ._models import TransferCallResultEvent  # type: ignore
    from ._models import TransferToCallRequest  # type: ignore
    from ._models import TransferToParticipantRequest  # type: ignore
    from ._models import UnmuteParticipantRequest  # type: ignore
    from ._models import UpdateAudioRoutingGroupRequest  # type: ignore

from ._azure_communication_calling_server_service_enums import (
    AudioRoutingMode,
    CallConnectionState,
    CallLocatorKindModel,
    CallMediaType,
    CallRecordingState,
    CallRejectReason,
    CallingEventSubscriptionType,
    CallingOperationStatus,
    CommunicationCloudEnvironmentModel,
    RecordingChannelType,
    RecordingContentType,
    RecordingFormatType,
    ToneValue,
)

__all__ = [
    'AddParticipantRequest',
    'AddParticipantResult',
    'AddParticipantResultEvent',
    'AddParticipantWithCallLocatorRequest',
    'AnswerCallRequest',
    'AnswerCallResult',
    'AudioRoutingGroupRequest',
    'AudioRoutingGroupResult',
    'CallConnectionProperties',
    'CallConnectionStateChangedEvent',
    'CallLocatorModel',
    'CallParticipant',
    'CallRecordingProperties',
    'CallRecordingStateChangeEvent',
    'CallingOperationResultDetails',
    'CancelMediaOperationWithCallLocatorRequest',
    'CancelParticipantMediaOperationRequest',
    'CancelParticipantMediaOperationWithCallLocatorRequest',
    'CommunicationError',
    'CommunicationErrorResponse',
    'CommunicationIdentifierModel',
    'CommunicationUserIdentifierModel',
    'CreateAudioRoutingGroupResult',
    'CreateCallRequest',
    'CreateCallResult',
    'GetAllParticipantsWithCallLocatorRequest',
    'GetParticipantRequest',
    'GetParticipantWithCallLocatorRequest',
    'HoldMeetingAudioRequest',
    'JoinCallRequest',
    'JoinCallResult',
    'MicrosoftTeamsUserIdentifierModel',
    'MuteParticipantRequest',
    'ParticipantsUpdatedEvent',
    'PhoneNumberIdentifierModel',
    'PlayAudioRequest',
    'PlayAudioResult',
    'PlayAudioResultEvent',
    'PlayAudioToParticipantRequest',
    'PlayAudioToParticipantWithCallLocatorRequest',
    'PlayAudioWithCallLocatorRequest',
    'RedirectCallRequest',
    'RejectCallRequest',
    'RemoveParticipantRequest',
    'RemoveParticipantWithCallLocatorRequest',
    'ResumeMeetingAudioRequest',
    'StartCallRecordingResult',
    'StartCallRecordingWithCallLocatorRequest',
    'ToneInfo',
    'ToneReceivedEvent',
    'TransferCallResult',
    'TransferCallResultEvent',
    'TransferToCallRequest',
    'TransferToParticipantRequest',
    'UnmuteParticipantRequest',
    'UpdateAudioRoutingGroupRequest',
    'AudioRoutingMode',
    'CallConnectionState',
    'CallLocatorKindModel',
    'CallMediaType',
    'CallRecordingState',
    'CallRejectReason',
    'CallingEventSubscriptionType',
    'CallingOperationStatus',
    'CommunicationCloudEnvironmentModel',
    'RecordingChannelType',
    'RecordingContentType',
    'RecordingFormatType',
    'ToneValue',
]
