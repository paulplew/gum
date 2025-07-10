# Gum | PL
A simple interpreted functional language implemented using python [`sly`](https://github.com/dabeaz/sly).

## System Requirements
- [`python3`[(https://www.python.org/downloads/)
- [`direnv`](https://direnv.net/) (optional)

## Setup
1. Activate python venv with `direnv allow` 
2. Install python requirements `pip install -r requirements.txt` 

## Usage
Run the interpreter after setup by executing `python src`
The prompt will appear:
```
gum >>
```
Programs must be typed on a single line and surrounded by curly brackets:
```
gum >> { a = 1; print(a); }
1
None
gum >>
```

## Testing
This project uses `pytest` and has a number of [sample scripts](tests/test_data) that are used for testing.

## Usage

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

### Examples
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

