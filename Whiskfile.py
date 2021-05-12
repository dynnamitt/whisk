from typing import List, Callable

# dont do this .. use a haskell type-alias
class Task:
    def __init__(self):
        pass

registry: List[Callable] = []


def register(fn: Callable) -> Callable:
    registry.append(fn)
    return fn

def inp(dep_func: Callable) -> Callable:
    val = dep_func()
    print("DEP_FUNC val = ",val)
    def decor (fn: Callable) -> Callable:
      def wrapper(*args, **kwargs):
           return fn(val)
      return wrapper

    return decor


@register
def fetch_root_pwd() -> Task:
    print("aws ssm get PWD")
    return "password"

@register
@inp(fetch_root_pwd)
def fetch_url(inp) -> Task:
    print("aws ssm geT url",inp)
    return "http://B"

@register
@inp(fetch_root_pwd)
def fetch_url2(inp) -> Task:
    print("aws ssm geT url",inp)
    return "http://A"

@register
@inp(fetch_url)
@inp(fetch_url2)
def exec(inp) -> Task:
    y = fetch_url()
    print("aws ssm get-",y)
    return {}


print(repr(registry))

exec()

