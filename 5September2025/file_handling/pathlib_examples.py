from pathlib import Path


if __name__ == "__main__":
    current = Path.cwd()
    print("Current:", current)
    for py in Path('.').glob('**/*.py'):
        if py.is_file():
            print(py) 