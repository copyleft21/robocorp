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

from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class StopProcessRunRequest(BaseModel):
    """
    StopProcessRunRequest
    """
    set_remaining_work_items_as_done: StrictBool = Field(...)
    terminate_ongoing_activity_runs: StrictBool = Field(...)
    reason: Optional[StrictStr] = None
    __properties = ["set_remaining_work_items_as_done", "terminate_ongoing_activity_runs", "reason"]

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
    def from_json(cls, json_str: str) -> StopProcessRunRequest:
        """Create an instance of StopProcessRunRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StopProcessRunRequest:
        """Create an instance of StopProcessRunRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StopProcessRunRequest.parse_obj(obj)

        _obj = StopProcessRunRequest.parse_obj({
            "set_remaining_work_items_as_done": obj.get("set_remaining_work_items_as_done"),
            "terminate_ongoing_activity_runs": obj.get("terminate_ongoing_activity_runs"),
            "reason": obj.get("reason")
        })
        return _obj


