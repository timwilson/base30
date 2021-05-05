# base30 – Python library for converting decimal to base30

This Python module has functions to convert a decimal number to a special form of base30 that reduces the number of characters required to represent the number while excluding vowels to reduce the likelihood of creating ambiguity between numeral and letters (e.g., "0" and "O") and inadvertently spelling words.

The characters representing the 30 digits in the base30 form include: `0123456789BCDFGHJKLMNPQRSTVWXZ`. Only capital letters are used to further reduce amiguity (e.g., "l" vs. "1").

## Installing

The module can be installed from GitHub via pip.

## Examples

The module has two functions: `dec_to_b30` and `b30_to_dec` which take a single number or string as an argument depending on which function you are using.

```
>>> from base30 import *
>>> dec_to_b30(20210505)
'SXJ3H'
>>> b30_to_dec("SXJ3H")
20210505
```
