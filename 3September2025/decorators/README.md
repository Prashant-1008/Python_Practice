## Decorators

File:
- `first.py`: Multiple decorator patterns.

### Covered
- Without wrapper: returns the original function unchanged.
- With wrapper (no parameters): print before call, then call the function.
- With wrapper and parameters: wrapper accepts args and forwards them.
- Immediate-call style (not recommended): calls the function during decoration time.
- Logging decorator: prints function name before calling.

### Why wrapper is needed
- A proper decorator must return a callable. If you call the function inside the decorator and return nothing, the decorated name becomes `None` and calling it later crashes.

### Run
```bash
python3 first.py
```

### Stretch
- Generalize wrappers with `*args, **kwargs` so they work for any signature.
- Preserve metadata with `functools.wraps`. 