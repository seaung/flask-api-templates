from functools import wraps
from typing import Any, Tuple
from flask import request

from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, verify_jwt_in_request


jwt = JWTManager()
identity = dict(uuid=0, scope="clams-jwt")


def login_required(fn: Any) -> Any:
    """
    验证jwt token
    """
    @wraps(fn)
    def wrapper(*args, **kwargs) -> Any:
        verify_jwt_in_request()
        return fn(*args, **kwargs)
    return wrapper


def get_tokens(user: Any, verify_remote_addr: bool = False) -> Tuple:
    """
    获取access_token和refresh_token
    """
    identity["uuid"] = user.id
    if verify_remote_addr:
        identity["remote_addr"] = request.remote_addr
    access_token = create_access_token(identity=identity)
    refresh_token = create_access_token(identity=identity)
    return access_token, refresh_token


def get_access_token(user: Any, scope: Any = None, 
                     fresh: bool = False, expires_delta: Any = None, 
                     verify_remote_addr: bool = False) -> str:
    """
    获取access_token
    """
    identity["uudi"] = user.id
    identity["scope"] = scope
    if verify_remote_addr:
        identity["remote_addr"] = request.remote_addr

    access_token = create_access_token(
            identity=identity,
            fresh=fresh,
            expires_delta=expires_delta
            )
    return access_token


def get_refresh_token(user: Any, scope: Any = None, 
                      expires_delta: Any = None, 
                      verify_remote_addr: bool = False) -> str:
    """
    获取refresh token
    """
    identity["uuid"] = user.id
    identity["scope"] = scope
    if verify_remote_addr:
        identity["remote_addr"] = request.remote_addr

    refresh_toekn = create_refresh_token(
            identity=identity,
            expires_delta=expires_delta
            )
    return refresh_toekn


@jwt.invalid_token_loader
def invalid_loader_callback(e: Any) -> Any:
    return "invalid token"


@jwt.expired_token_loader
def expired_token_callback(e: Any):
    return "expired token"

