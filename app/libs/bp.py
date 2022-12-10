from typing import Any


class BP(object):
    def __init__(self, name: str, prefix: bool = True) -> None:
        self.name = name
        self.prefix = prefix
        self.mount = []

    def route(self, rule: Any, **options) -> Any:
        def decorator(fn):
            self.mount.append((fn, rule, options))
            return fn
        return decorator

    def register(self, bp: Any, url_prefix: Any = None) -> None:
        if url_prefix is None and self.prefix:
            url_prefix = "/" + self.name
        else:
            url_prefix = "" + str(url_prefix) + "/" + self.name
        for f, rule, options in self.mount:
            endpoint = self.name + "+" + options.pop("endpoint", f.__name__)
            if rule:
                url = url_prefix + rule
                bp.add_url_rule(url, endpoint, f, **options)
            else:
                bp.add_url_rule(url_prefix, endpoint, f, **options)

