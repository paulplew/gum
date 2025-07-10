import os


def debuggable(func):
    def wrapper(*args, **kwargs):
        try:
            if bool(os.environ["DEBUG"]):
                print(f"vars: {vars(args[0])}")
                print(f"type: {type(args[0])}")
        except KeyError:
            pass

        result = func(*args, **kwargs)
        return result

    return wrapper
