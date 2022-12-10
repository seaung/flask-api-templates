from typing import Any
from app.libs.bp import BP


demon = BP("demon")


@demon.route("/demon", methods=["GET"])
def get_demon() -> Any:
    return "this is demon"

