def announce(f):
    def wrapper():
        print("Function is ready...")
        f()
        print("Function done!")
    return wrapper


@announce
def hello():
    print("Hello, world!")


hello()
