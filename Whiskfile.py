from typing import List, Callable

# dont do this .. use a haskell type-alias
class Task:
    def __init__(self):
        pass

registry: List[Callable] = []



# BATCH SHIT crazy framework DSL



def framework(id,opts):
    """ the smarness here """
    return id,opts

def resource(id):
    def decor(fn: Callable) -> Callable:
        registry.append(fn)
        def wrapper(*args,**kwargs):
            options = fn(*args,**kwargs)
            # merge options
            mix = {"shit":"out", **options}
            return framework(id,mix)
        return wrapper
    return decor

    return wrapper

def inp(*args) -> Callable:
    val = [fn() for fn in args]
    print("DEP_FUNC val = ",val)
    def decor (fn: Callable) -> Callable:
      def wrapper(*args, **kwargs):
           return fn(val)
      return wrapper

    return decor


@resource("aws.ssm.param")
def fetch_root_pwd() -> Task:
    print("aws ssm get PWD")
    return { "key":"/pwd"}

@resource("aws.ssm.param")
@inp(fetch_root_pwd)
def fetch_url(inp) -> Task:
    print("aws ssm geT url",inp)
    return {"key":"/A"}

@resource("aws.ssm.param")
@inp(fetch_root_pwd)
def fetch_url2(inp) -> Task:
    print("aws ssm geT url",inp)
    return {"key":"/B"}

@inp(fetch_url,fetch_url2)
def exec(inp) -> Task:
    print("aws ssm get-",inp)
    return {}


print(repr(registry))

exec()

