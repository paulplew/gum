# Gum | PL
A simple interpreted functional language implemented using `sly`.

## Quick Start
### Variable Definition
```
foo = 1;
bar = "gum";
baz = False;
```
### Function Definition
```
fun a(args) =
{
    ...
}
```
### Builtins
```
print("Hello World!");
```
### Conditionals
```
foo = 1;
if (foo == 1) 
{
    ...
}
```
### Loops
```
foo = 10;
while (foo >= 0) 
{
    print(foo);
    foo = foo - 1;
}
```

## System Requirements
```direnv, python3```

## Setup
1. Activate python venv with `direnv allow` 
2. Install python requirements `pip install -r requirements.txt` 

## Testing
This project uses `pytest` and has some sample scripts in `tests/test_data`.
