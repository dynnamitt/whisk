from typing import List, Callable

registry: List[Callable] = []
def register(fn: Callable) -> Callable:
    registry.append(fn)
    return fn

@register
def fetch_root_pwd() -> None:
    print("aws ssm get-")


print(registry)