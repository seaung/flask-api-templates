from typing import Any
from flask import request
from wtforms import Form

from app.libs.exceptions import ParamterException


class BaseForms(Form):
    def __init__(self) -> None:
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForms, self).__init__(data=data, **args)

    def validate_for_api(self) -> Any:
        valid = super(BaseForms, self).validate()
        if not valid:
            raise ParamterException(msg=self.errors)
        return self


