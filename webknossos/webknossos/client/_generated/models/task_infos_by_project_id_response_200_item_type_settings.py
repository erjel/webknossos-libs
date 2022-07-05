from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.task_infos_by_project_id_response_200_item_type_settings_resolution_restrictions import (
    TaskInfosByProjectIdResponse200ItemTypeSettingsResolutionRestrictions,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskInfosByProjectIdResponse200ItemTypeSettings")


@attr.s(auto_attribs=True)
class TaskInfosByProjectIdResponse200ItemTypeSettings:
    """ """

    allowed_modes: List[str]
    branch_points_allowed: int
    soma_clicking_allowed: int
    merger_mode: int
    resolution_restrictions: TaskInfosByProjectIdResponse200ItemTypeSettingsResolutionRestrictions
    volume_interpolation_allowed: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowed_modes = self.allowed_modes

        branch_points_allowed = self.branch_points_allowed
        soma_clicking_allowed = self.soma_clicking_allowed
        merger_mode = self.merger_mode
        resolution_restrictions = self.resolution_restrictions.to_dict()

        volume_interpolation_allowed = self.volume_interpolation_allowed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowedModes": allowed_modes,
                "branchPointsAllowed": branch_points_allowed,
                "somaClickingAllowed": soma_clicking_allowed,
                "mergerMode": merger_mode,
                "resolutionRestrictions": resolution_restrictions,
            }
        )
        if volume_interpolation_allowed is not UNSET:
            field_dict["volumeInterpolationAllowed"] = volume_interpolation_allowed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allowed_modes = cast(List[str], d.pop("allowedModes"))

        branch_points_allowed = d.pop("branchPointsAllowed")

        soma_clicking_allowed = d.pop("somaClickingAllowed")

        merger_mode = d.pop("mergerMode")

        resolution_restrictions = TaskInfosByProjectIdResponse200ItemTypeSettingsResolutionRestrictions.from_dict(
            d.pop("resolutionRestrictions")
        )

        volume_interpolation_allowed = d.pop("volumeInterpolationAllowed", UNSET)

        task_infos_by_project_id_response_200_item_type_settings = cls(
            allowed_modes=allowed_modes,
            branch_points_allowed=branch_points_allowed,
            soma_clicking_allowed=soma_clicking_allowed,
            merger_mode=merger_mode,
            resolution_restrictions=resolution_restrictions,
            volume_interpolation_allowed=volume_interpolation_allowed,
        )

        task_infos_by_project_id_response_200_item_type_settings.additional_properties = (
            d
        )
        return task_infos_by_project_id_response_200_item_type_settings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
