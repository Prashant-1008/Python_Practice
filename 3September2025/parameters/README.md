## Parameters and Arguments

Files:
- `basics.py`: Positional arguments, and the meaning of parameter vs argument.
- `parameters.py`: Multiple definitions to illustrate positional, `*args`, `**kwargs`, and combining them.

### Key ideas
- Positional parameters: order matters.
- `*args`: variable-length positional arguments (tuple).
- `**kwargs`: variable-length keyword arguments (dict).
- Resolution order: positional → `*args` → keyword → `**kwargs`.

### Run
```bash
python3 basics.py
python3 parameters.py
```

### Tips
- When mixing, use: `def f(positional, *args, keyword=None, **kwargs): ...`
- Avoid redefining the same function name unless you intend to override it in the same file (later definition wins). 