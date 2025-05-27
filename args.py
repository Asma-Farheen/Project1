def f(*args, **kwargs):
    x = args[0]
    y = kwargs.get("y")
    print(f"x: {x},y: {y}")
f(5,y=2)