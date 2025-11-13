# JargonLang
Version 0.16.0 (2025/11/13)

File extension: .jgl

Contains a lexer and a parser.

Types: int, float, str, char
# Operations: 
## Addition `a+b`
Adds `a` and `b`
## Subtraction `a-b`
Subtracts `b` from `a`
## Comparisons `a>b`, `a<b`, `a<=b`, `a>=b`
Compares `a` and `b` and returns a result depending on the larger value
## Equality `a==b`
Sees if `a` and `b` have the same value
## Inequality `a!=b`
Sees if `a` and `b` do not have the same value
## Subtraction `a-b`
Subtracts `b` from `a`
## Negation `-a`
Returns the additive inverse of `a`
## Assignment `a=b`
Assigns the value `b` to variable `a`
## Code blocks `{}`
Creates a block of multiple statements separated by semicolons. 
## Function calls `a(b, c)`
Used to call function `a` with arguments in parentheses
# Keywords
## `var`
```
var x: int = 5
```
```
var x: float
```
Used to declare a variable. The type is mandatory, but you dont have to assign a value.
## `func`
```
func f(a: int, b: str) -> int { var x = 5; }
Used to declare a function. You must specify the name, return type and the types of the arguments, but you dont have to add arguments.
## `return`
```
return x;
```
Used to return a value from a function.
# Misc
## Parentheses `(a)`
https://study.com/learn/lesson/parentheses-math-rules-examples.html
## Bitwise OR `a|b`
Performs a bitwise OR operation on `a` and `b`
TODO
## Comment `//text`
Ignores text until the end of the line
## Multiline comment `/*a*/`
Ignores text until the end of the file or `*/`
# Order of operations
Highest priority first
- Assignment (=) 
- Function calls (f())
- Unary operations (-, !, ~)
- Multiplication and division (*, /)
- Binary bitwise operations (|, &, ^)
- Addition and subtraction (+, -)
- Comparisons(>, <, >=, <=)
- Binary logical operations (||, &&)
- Equality and inequality (==, !=)
