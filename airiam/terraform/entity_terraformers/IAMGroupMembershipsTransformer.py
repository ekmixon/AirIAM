from airiam.terraform.entity_terraformers.BaseEntityTransformer import BaseEntityTransformer

import json


class IAMGroupMembershipsTransformer(BaseEntityTransformer):
    def __init__(self, entity_json: dict):
        super().__init__('aws_iam_group_membership', f"{entity_json['GroupName']}_membership", entity_json)
        self._users = entity_json['Users']

    def _generate_hcl2_code(self, entity_json) -> str:
        return f"""resource "aws_iam_group_membership" "{self._safe_name}" {{
  name = "{self._safe_name}"
  group = {entity_json['GroupHcl']}.name
  users = {json.dumps(entity_json['Users'])}
}}

"""

    def entities_to_import(self) -> list:
        return [
            {
                "identifier": f"{self.identifier()}[i]",
            }
            for _ in range(len(self._users))
        ]
