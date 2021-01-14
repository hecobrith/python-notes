# Numbers

Python offers us a broad set of arithmetic operators: ```+, -, *, /, //, %, and **.``` The / and // operators are for division; we'll look at these in a separate recipe named Choosing between true division and floor division. The ** operator raises a number to a power.

For dealing with individual bits, we have some additional operations. We can use ```&, ^, |, <<, and >>```. These operators work bit by bit on the internal binary representations of integers. These compute a binary AND, a binary Exclusive OR, Inclusive OR, Left Shift, and Right Shift respectively.

There are three general cases for math that involve numbers beyond integers, which are:

- Currency: Dollars, cents, euros, and so on. Currency generally has a fixed number of decimal places. Rounding rules are used to determine what 7.25% of $2.95 is, rounded to the nearest penny.

```python
from decimal import 
tax_rate = Decimal('7.25')/Decimal(100)
purchase_amount = Decimal('2.95')
tax_rate * purchase_amount
```

- Rational Numbers or Fractions: When we're working with American units like feet and inches, or cooking measurements in cups and fluid ounces, we often need to work in fractions. When we scale a recipe that serves eight, for example, down to five people, we're doing fractional math using a scaling factor of 5/8. How do we apply this scaling to 2/3 cup of rice and still get a measurement that fits an American kitchen gadget?
```python
from fractions import Fraction
sugar_cups = Fraction('2.5')
scale_factor = Fraction(5/8)
sugar_cups * scale_factor
```
- Irrational Numbers: This includes all other kinds of calculations. It's important to note that digital computers can only approximate these numbers, and we'll occasionally see odd little artifacts of this approximation. Float approximations are very fast, but sometimes suffer from truncation issues.

There are several general cases for division:

- A div-mod pair: We want both parts – the quotient and the remainder. The name refers to the division and modulo operations combined together. We can summarize the quotient and remainder as .
We often use this when converting values from one base into another. When we convert seconds into hours, minutes, and seconds, we'll be doing a
- div-mod kind of division. We don't want the exact number of hours; we want a truncated number of hours, and the remainder will be converted into minutes and seconds.

- The true value: This is a typical floating-point value; it will be a good approximation to the quotient. For example, if we're computing an average of several measurements, we usually expect the result to be floating-point, even if the input values are all integers.
A rational fraction value: This is often necessary when working in American units of feet, inches, and cups. For this, we should be using the Fraction class. When we divide Fraction objects, we always get exact answers.

# Strings

We can't—technically—modify a string in place. The data structure for a string is immutable. However, we can assign a new string back to the original variable. This technique behaves the same as modifying a string in place.

When a variable's value is replaced, the previous value no longer has any references and is garbage collected. We can see this by using the id() function to track each individual string object

```python
>>> title = "Recipe 5: Rewriting, and the Immutable String"
>>> title[8] = ''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

Since we can't replace characters in a string object, we have to work out some alternatives. There are several common things we can do, shown as follows:

- A combination of slicing and concatenating a string to create a new string.
- When shortening, we often use the partition() method.
- We can replace a character or a substring with the replace() method.
- We can expand the string into a list of characters, then join the string back into a single string again. This is the subject of a separate recipe, Building complex strings with a list of characters.


The index function locates a particular substring and returns the position where that substring can be found. If the substring doesn't exist, it raises an exception. The following expression will always be true: ```title[colon_position] == ':'```.
```python
colon_position = title.index(':')
discard, post_colon = title[:colon_position], title[colon_position+1:]

# also partition method
pre_colon_text, _, post_colon_text = title.partition(':')
```

#### replacemnt method

We can use a string's replace() method to create a new string with punctuation marks removed. When using replace to switch punctuation marks, save the results back into the original variable. In this case, post_colon_text:

```python
post_colon_text = post_colon_text.replace(' ', '_')
post_colon_text = post_colon_text.replace(' ', '_')
post_colon_text
```

This has replaced the two kinds of punctuation with the desired _ characters. We can generalize this to work with all punctuation
not only the character selected

```python
from string import whitespace, punctuation

for character in whitespace + punctuation:
    post_colon_text = post_colon_text.replace(character, '_')

print(post_colon_text)
>>>'_Rewriting__and_the_Immutable_String'
```

We can also use a string's translate() method for this. This relies on creating a dictionary object to map each source character's position to a resulting character:

```python
from string import whitespace, punctuation
title = "Recipe 5: Rewriting an Immutable String"
title.translate({ord(c): '_' for c in whitespace+punctuation})
>>> Recipe_5__Rewriting_an_Immutable_String
```

#### Removing extra punctuation

```python
post_colon_text = post_colon_text.strip('_')
# to get all the _
while '__' in post_colon_text:
    post_colon_text = post_colon_text.replace('__', '_')
```

## String parse with Regex

We've replaced representation hints such as ingredient words, a mixture of letters and spaces, with [\w\s]+. We've replaced amount digits with \d+. And we've replaced single spaces with \s+ to allow one or more spaces to be used as punctuation. We've left the colon in place because, in the regular expression notation, a colon matches itself.

For each of the fields of data, we've used () to capture the data matching the pattern. We didn't capture the colon or the spaces because we don't need the punctuation characters.

REs typically use a lot of \ characters. To make this work out nicely in Python, we almost always use raw strings. The r' prefix tells Python not to look at the \ characters and not to replace them with special characters that aren't on our keyboards.

```python
ingredient = "Kumquat: 2 cups"
(ingredient words): (amount digits) (unit words)

import re
ingredient_pattern = re.compile(r'([\w\s]+):\s+(\d+)\s+(\w+)')
pattern = re.compile(pattern_text)
match = pattern.match(ingredient)
match.groups()
>>> ('Kumquat', '2', 'cups')
match.group(1)
>>> 'Kumquart'
match.group(3)
>>> 'cups
```

- \w matches any alphanumeric character (a to z, A to Z, 0 to 9)
- \d matches any decimal digit
- \s matches any space or tab character
- \W matches any character that's not a letter or a digit
- \D matches any character that's not a digit
- \S matches any character that's not some kind of space or tab

- We saw that + as a suffix means to match one or more of the preceding patterns. \d+ matches one or more digits. To match an ordinary +, we need to use \+.
- We also have * as a suffix, which matches zero or more of the preceding patterns. \w* matches zero or more characters. To match a *, we need to use \*.
- We have ? as a suffix, which matches zero or one of the preceding expressions. This character is used in other places, and has a different meaning in the other context. We'll see it used in (?P<name>...), where it is inside () to define special properties for the grouping.
- . matches any single character. To match a . specifically, we need to use \..

We can create our own unique sets of characters using [] to enclose the elements of the set
```python
(?P<name>\w+)\s*[=:]\s*(?P<value>.*)
#these will get strings like this
size = 12 
weight: 14
```

1. This has a \w+ to match any number of alphanumeric characters. This will be collected into a group called name.
2. It uses \s* to match an optional sequence of spaces.
3. It matches any character in the set [=:]. Exactly one of the characters in this set must be present.
4. It uses \s* again to match an optional sequence of spaces
5. Finally, it uses .* to match everything else in the string. This is collected into a group named 

## F String

[Further references](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals)

f-strings can do a lot of relatively sophisticated string assembly by interpolating data into a template. There are a number of conversions available.

- b is for binary, base 2.
- c is for Unicode character. The value must be a number, which is converted into a character. Often, we use hexadecimal numbers for these characters, so you might want to try values such as 0x2661 through 0x2666 to see interesting Unicode glyphs.
- d is for decimal numbers.
- E and e are for scientific notations. 6.626E-34 or 6.626e-34, depending on which E or e character is used.
- F and f are for floating-point. For not a number, the f format shows lowercase nan; the F format shows uppercase NAN.
- G and g are for general use. This switches automatically between E and F (or e and f) to keep the output in the given sized field. For a format of 20.5G, up to 20-digit numbers will be displayed using F formatting. Larger numbers will use E formatting.
- n is for locale-specific decimal numbers. This will insert , or . characters, depending on the current locale settings. The default locale may not have 1,000 separators defined. For more information, see the locale module.
- o is for octal, base 8.
- s is for string.
- X and x are for hexadecimal, base 16. The digits include uppercase A-F and lowercase a-f, depending on which X or x format character is used.
- % is for percentage. The number is multiplied by 100 and includes the %.
---
- Fill and alignment: We can specify a specific filler character (space is the default) and an alignment. Numbers are generally aligned to the right and strings to the left. We can change that using <, >, or ^. This forces left alignment, right alignment, or centering, respectively. There's a peculiar = alignment that's used to put padding after a leading sign.
- Sign: The default rule is a leading negative sign where needed. We can use + to put a sign on all numbers, - to put a sign only on negative numbers, and a space to use a space instead of a plus for positive numbers. In scientific output, we often use {value: 5.3f}. The space makes sure that room is left for the sign, ensuring that all the decimal points line up nicely.
- Alternate form: We can use the # to get an alternate form. We might have something like {0:#x}, {0:#o}, or {0:#b} to get a prefix on hexadecimal, octal, or binary values. With a prefix, the numbers will look like 0xnnn, 0onnn, or 0bnnn. The default is to omit the two-character prefix.
- Leading zero: We can include 0 to get leading zeros to fill in the front of a number. Something like {code:08x} will produce a hexadecimal value with leading zeroes to pad it out to eight characters.
- Width and precision: For integer values and strings, we only provide the width. For floating-point values, we often provide width.precision.
---
- {name!r} shows the representation that would be produced by repr(name).
- {name!s} shows the string value that would be produced by str(name); this is the default behavior if you don't specify any conversion. Using !s explicitly lets you add string-type format specifiers.
- {name!a} shows the ASCII value that would be produced by ascii(name).

## Using the Unicode

[list of Unicode](https://www.unicode.org/charts/) <br>
[wiki list](https://en.wikipedia.org/wiki/List_of_Unicode_characters)

A given font on our computer may not be designed to provide glyphs for all of those characters. In particular, Windows computer fonts may have trouble displaying some of these characters. Using the following Windows command to change to code page 65001 is sometimes necessary

```python
print('You Rolled \u2680')
print('You drew \u0001F000')
print('Discard \N{MAHJONG TILE RED DRAGON}')
```

Yes, we can include a wide variety of characters in Python output. To place a \ character in the string, we need to use \\. For example, we might need this for Windows file paths.

## Encoding strings – creating ASCII and UTF-8 bytes

We can make a general setting using the PYTHONIOENCODING environment variable. We set this outside of Python to ensure that a particular encoding is used everywhere. When using Linux or macOS, use export to set the environment variable. For Windows, use the set command, or the PowerShell Set-Item cmdlet. For Linux, it looks like this

```python
with open('some_file.txt', 'w', encoding='utf-8') as output:
     print( 'You drew \U0001F000', file=output )

with open('some_file.txt', 'r', encoding='utf-8') as input:
    text = input.read()

string_bytes = 'You drew \U0001F000'.encode('utf-8')
print(string_bytes)
>>> b'You drew \xf0\x9f\x80\x80'
```

Unicode defines a number of encoding schemes. While UTF-8 is the most popular, there is also UTF-16 and UTF-32. The number is the typical number of bits per character. A file with 1,000 characters encoded in UTF-32 would be 4,000 8-bit bytes. A file with 1,000 characters encoded in UTF-8 could be as few as 1,000 bytes, depending on the exact mix of characters. In UTF-8 encoding, characters with Unicode numbers above U+007F require multiple bytes.

Bytes versus strings: Bytes are often displayed using printable characters. We'll see b'hello' as shorthand for a five-byte value. The letters are chosen using the old ASCII encoding scheme, where byte values from 0x20 to 0x7F will be shown as characters, and outside this range, more complex-looking escapes will be used.

This use of characters to represent byte values can be confusing. The prefix of b' is our hint that we're looking at bytes, not proper Unicode characters.

## decodng - get proper characters from some bytes

Because the displayed value starts with b', it's bytes, not proper Unicode characters. It was probably encoded with UTF-8, which means some characters could have weird-looking \xnn escape sequences instead of proper characters. We want to have the proper characters.

While this data has many easy-to-read characters, the b' prefix shows that it's a collection of byte values, not proper text. Generally, a bytes object behaves somewhat like a string object. Sometimes, we can work with bytes directly. Most of the time, we'll want to decode the bytes and create proper Unicode characters from them.
```python
import urllib.request
warnings_uri= 'https://forecast.weather.gov/product.php?site=CRH&issuedby=AKQ&product=SMW&format=TXT'

with urllib.request.urlopen(warnings_uri) as source:
    warnings_text = source.read()

warnings_text[:80]
>>> b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.or'
document = forecast_text.decode("UTF-8")
```

## tuples

Tuples are one example of the more general Sequence class. We can do a few things with sequences.

```python
t = ('Kumquat', '2', 'cups')
len(t)
# How many times does a particular value appear in t?
t.count('2')
# Which position has a particular value?
t.index('cups')
# Does a particular value exist?
'Rice' in t
```
When we worked with tuples, we had to remember the positions as numbers.
```python
from typing import NamedTuple

class Ingredient(NamedTuple):
    ingredient: str
    amount: str
    unit: str

item_2 = Ingredient('Kumquat', '2', 'cups')
Fraction(item_2.amount)
Fraction(2, 1)
print(f"Use {item_2.amount} {item_2.unit} fresh {item_2.ingredient}")
>>> 'Use 2 cups fresh Kumquat'

class IngredientF(NamedTuple):
     ingredient: str
     amount: Fraction
     unit: str

item_3 = IngredientF('Kumquat', Fraction('2'), 'cups')
```