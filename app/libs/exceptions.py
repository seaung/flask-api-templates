from typing import Any
from flask import json, request
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = "服务端错误"
    error_code = 10000
    
    def __init__(self, msg: Any = None, 
                 code: Any = None, error_code: Any = None,
                 headers: Any = None) -> None:
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg

        if headers is not None:
            _headers = headers.copy()
            _headers.update(self.headers)
            self.headers = _headers
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ: Any = None) -> Any:
        body = dict(
                msg=self.msg,
                error_code=self.error_code,
                request=request.method + " " + self.get_url_no_param()
        )

        text = json.dumps(body)

        return text

    @staticmethod
    def get_url_no_param() -> str:
        full_path = str(request.full_path)
        main_path = full_path.split("?")
        return main_path[0]
