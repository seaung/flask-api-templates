from flask import Blueprint
from app.api.v1 import demo

def create_blueprint_v1() -> Blueprint:
    """注册蓝图"""
    bp_v1 = Blueprint("v1", __name__)
    demo.demon.register(bp_v1)
    return bp_v1
