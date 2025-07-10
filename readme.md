# Gum | PL
A simple interpreted functional language implemented using python [`sly`](https://github.com/dabeaz/sly).

## Recursive Factorial
```
fun fact(num) = 
{
  numFactorial = 0;
  if (num < 1)
  {
    numFactorial = 1;
  }
  else
  {
    numFactorial = num * fact(num-1);
  }
  return numFactorial;
}
```

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
This project uses `pytest` and has a number of [sample scripts](tests/test_data) that are used for testing.
