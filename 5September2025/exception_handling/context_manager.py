from contextlib import contextmanager


@contextmanager
def managed_resource(name: str):
    print(f"Acquiring {name}")
    try:
        yield f"resource({name})"
    finally:
        print(f"Releasing {name}")


if __name__ == "__main__":
    with managed_resource("demo") as res:
        print("Using", res)
    # with for file automatically handles close
    with open(__file__, "r", encoding="utf-8") as f:
        _ = f.readline() 