# coding: utf-8

"""
    Robocorp Control Room API

    Robocorp Control Room API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

import pydantic

from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from robocorp.workspace.models.task_package_resource_download import TaskPackageResourceDownload
from robocorp.workspace.models.update_worker_request import UpdateWorkerRequest

class TaskPackageResource(BaseModel):
    """
    TaskPackageResource
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    type: StrictStr = Field(...)
    tasks: conlist(UpdateWorkerRequest) = Field(..., description="Tasks contained in the task package: empty array if the task package has not been uploaded yet.")
    download: Optional[TaskPackageResourceDownload] = Field(...)
    __properties = ["id", "name", "type", "tasks", "download"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('zip'):
            raise ValueError("must be one of enum values ('zip')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TaskPackageResource:
        """Create an instance of TaskPackageResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tasks (list)
        _items = []
        if self.tasks:
            for _item in self.tasks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tasks'] = _items
        # override the default output from pydantic by calling `to_dict()` of download
        if self.download:
            _dict['download'] = self.download.to_dict()
        # set to None if download (nullable) is None
        # and __fields_set__ contains the field
        if self.download is None and "download" in self.__fields_set__:
            _dict['download'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskPackageResource:
        """Create an instance of TaskPackageResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskPackageResource.parse_obj(obj)

        _obj = TaskPackageResource.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "tasks": [UpdateWorkerRequest.from_dict(_item) for _item in obj.get("tasks")] if obj.get("tasks") is not None else None,
            "download": TaskPackageResourceDownload.from_dict(obj.get("download")) if obj.get("download") is not None else None
        })
        return _obj


