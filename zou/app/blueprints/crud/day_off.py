from zou.app.models.day_off import DayOff
from zou.app.models.time_spent import TimeSpent

from zou.app.blueprints.crud.base import BaseModelsResource, BaseModelResource

from zou.app.services import user_service, time_spents_service

from zou.app.services.exception import ArgumentsException


class DayOffsResource(BaseModelsResource):
    def __init__(self):
        BaseModelsResource.__init__(self, DayOff)

    def check_create_permissions(self, data):
        return user_service.check_day_off_access(data)

    def check_creation_integrity(self, data):
        if time_spents_service.get_day_offs_between(
            data["date"], data["end_date"], data["person_id"]
        ):
            raise ArgumentsException("Day off already exists for this period")
        return data

    def post_creation(self, instance):
        TimeSpent.delete_all_by(
            instance.date >= TimeSpent.date,
            instance.end_date <= TimeSpent.date,
            person_id=instance.person_id,
        )
        return instance.serialize()


class DayOffResource(BaseModelResource):
    def __init__(self):
        BaseModelResource.__init__(self, DayOff)

    def check_delete_permissions(self, instance_dict):
        return user_service.check_day_off_access(instance_dict)

    def check_read_permissions(self, instance):
        return user_service.check_day_off_access(instance)

    def post_update(self, instance_dict, data):
        TimeSpent.delete_all_by(
            instance_dict["date"] >= TimeSpent.date,
            instance_dict["end_date"] <= TimeSpent.date,
            person_id=instance_dict["person_id"],
        )
        return instance_dict

    def pre_update(self, instance_dict, data):
        if time_spents_service.get_day_offs_between(
            data.get("date", instance_dict["data"]),
            data.get("end_date", instance_dict["end_date"]),
            data.get("person_id", instance_dict["person_id"]),
        ):
            raise ArgumentsException("Day off already exists for this period")
        return data
