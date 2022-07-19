# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import ConfidentialLedgerCertificateClientConfiguration
from ._operations import ConfidentialLedgerCertificateClientOperationsMixin
from ._serialization import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict


class ConfidentialLedgerCertificateClient(
    ConfidentialLedgerCertificateClientOperationsMixin
):  # pylint: disable=client-accepts-api-version-keyword
    """The ConfidentialLedgerCertificateClient is used to retrieve the TLS certificate required for
    connecting to a Confidential Ledger.

    :param certificate_endpoint: The certificate endpoint (or "Identity Service Endpoint" in the
     Azure portal), for example https://identity.confidential-ledger.core.azure.com. Required.
    :type certificate_endpoint: str
    :keyword api_version: Api Version. Default value is "2022-05-13". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, certificate_endpoint: str, **kwargs: Any
    ) -> None:
        _endpoint = "{certificateEndpoint}"
        self._config = ConfidentialLedgerCertificateClientConfiguration(
            certificate_endpoint=certificate_endpoint, **kwargs
        )
        self._client = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "certificateEndpoint": self._serialize.url(
                "self._config.certificate_endpoint", self._config.certificate_endpoint, "str", skip_quote=True
            ),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> ConfidentialLedgerCertificateClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
