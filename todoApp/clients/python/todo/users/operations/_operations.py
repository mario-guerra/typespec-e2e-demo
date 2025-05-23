# coding=utf-8

from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from .. import models as _models1
from ... import models as _models2
from ..._configuration import TodoClientConfiguration
from ..._model_base import SdkJSONEncoder, _deserialize, _failsafe_deserialize
from ..._serialization import Deserializer, Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_users_create_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/users"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class UsersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~todo.TodoClient`'s
        :attr:`users` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: TodoClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def create(
        self, user: _models2.User, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.CreateResponse:
        """create.

        :param user: Required.
        :type user: ~todo.models.User
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CreateResponse. The CreateResponse is compatible with MutableMapping
        :rtype: ~todo.models.CreateResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(self, user: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models2.CreateResponse:
        """create.

        :param user: Required.
        :type user: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CreateResponse. The CreateResponse is compatible with MutableMapping
        :rtype: ~todo.models.CreateResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self, user: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models2.CreateResponse:
        """create.

        :param user: Required.
        :type user: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CreateResponse. The CreateResponse is compatible with MutableMapping
        :rtype: ~todo.models.CreateResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def create(self, user: Union[_models2.User, JSON, IO[bytes]], **kwargs: Any) -> _models2.CreateResponse:
        """create.

        :param user: Is one of the following types: User, JSON, IO[bytes] Required.
        :type user: ~todo.models.User or JSON or IO[bytes]
        :return: CreateResponse. The CreateResponse is compatible with MutableMapping
        :rtype: ~todo.models.CreateResponse
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models2.CreateResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(user, (IOBase, bytes)):
            _content = user
        else:
            _content = json.dumps(user, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_users_create_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = None
            if response.status_code == 409:
                error = _failsafe_deserialize(_models1.UserExistsResponse, response.json())
                raise ResourceExistsError(response=response, model=error)
            elif response.status_code == 422:
                error = _failsafe_deserialize(_models1.InvalidUserResponse, response.json())
            elif 400 <= response.status_code <= 499:
                error = _failsafe_deserialize(_models2.Standard4XXResponse, response.json())
            elif 500 <= response.status_code <= 599:
                error = _failsafe_deserialize(_models2.Standard5XXResponse, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models2.CreateResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
