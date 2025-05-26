# loopypy
The official Python wrapper for api.loopy5418.dev.
Install with:
```bash
pip install loopypy
```
The usage is very human:
You can do either
```python
import loopypy
```
or
```python
from loopypy import setApiKey, ...
```
both are supported.

Set your api key using `setApiKey(key)`.

Function List:
---
|Name|Description|API Key|
|----|-----------|-------|
|`setApiKey(key)`|Sets the API key for automated gathering later on.|x|
|`getApiKey()`|Returns the API key|Required|
|`ai(prompt, speed)`|Uses the /openai/text endpoint to generate text from ChatGPT.|Required|
|`owoify(text)`|Owoifies the text and returns it|Optional|
|`emojify(text)`|Turns the text into regional indicators in Discord format.|Optional|
|`qr(data)`|Turns the given data into a QR code and returns the image buffer.|Required|
|`currency(base, target, amount)`|Converts  one currency to another.|Required|
|`seconds_to_time(seconds)`|Converts given seconds into formatted time (HH\:MM:SS)|Optional|
|`pick(*args)`|Picks an option off of the given ones.|Optional|
|`ascii_art(text)`|Returns multiline ascii art off of the given text.|Optional|
|`Coming Soon`|More functions are coming soon.|

Usages:
---
```python
setApiKey(key)
```
Sets the API key for later use. Required for most endpoints.
Syntax:
- `key`: string, required

### Example Usage:
```python
import loopypy
loopypy.setApiKey("xxxxx-xxxxxx-xxxxx-xxxxx")
print(loopypy.getApiKey()) # Prints the key you set
```
---
```python
getApiKey()
```
Retrieves and returns the current API key.
Example Usage:
```python
import loopypy
loopypy.setApiKey("xxxxx-xxxxxx-xxxxx-xxxxx")
print(loopypy.getApiKey()) # Prints the key you set
```
---
```python
ai(prompt, speed)
```
Uses the /openai/text endpoint to generate text from ChatGPT.
Syntax:
- `prompt`: String, required
- `speed`: Integer, optional, defaults to 1. (0: large, 1: balanced, 2: fast)
Children:
- `.response`
- `.model`
- `.prompt`
- `.success`
Example Usage:
```python
import loopypy
loopypy.setApiKey("xxxxx-xxxxxx-xxxxx-xxxxx")
ask = loopypy.ai("What's the capital of France?")
print(f"Response: {ask.response}")
print(f"Model: {ask.model}")
```
---
```python
owoify(text)
```
Owoifies the text and returns it.
Syntax:
- `text`: string, required
Example Usage:
```python
import loopypy
print(loopypy.owoify("Hello!"))
```
---
```python
emojify(text)
```
Turns the text into regional indicators in Discord format.
Syntax:
- `text` string, required
Example Usage:
```python
import loopypy
print(loopypy.emojify("Hello")) # Prints the key you set
```
---
```python
qr(data)
```
Turns the given data into a QR code and returns the image buffer.
Syntax:
- `data`: string, required
Example Usage:
```python
import loopypy
loopypy.setApiKey("xxxxx-xxxxxx-xxxxx-xxxxx")
buffer = loopypy.qr("Hello!") # get image buffer
with open("image.png", "wb") as f:
    f.write(buffer)
    print("QR Code image saved to file!")
```
---
```python
currency(base, target, amount)
```
Converts  one currency to another.
Syntax:
- `base`: string, required
- `target`: string, required
- `amount`: integer, required
Children:
- `.rate`
- `.converted`
- `.success`
Example Usage:
```python
import loopypy
loopypy.setApiKey("xxxxx-xxxxxx-xxxxx-xxxxx")
cur = loopypy.currency("USD", "EUR", 1)
print(f"Converted Money: {cur.converted}")
print(f"Rate: {cur.rate}")
```
---
```python
seconds_to_time(seconds)
```
-# This function will soon be changed to fit the children system. E.g. print(seconds_to_time.seconds)
Converts given seconds into formatted time (HH\:MM:SS)
Syntax:
- `seconds` integer, required
Example Usage:
```python
import loopypy
seconds = 260 # is 4 minutes and 20 seconds
print(loopypy.seconds_to_time(seconds)) # prints 00:04:20
```
---
```python
pick(*args)
```
Picks one of the given options.
Syntax:
- `args`: multiple objects, required
Example Usage:
```python
import loopypy
print(loopypy.pick("Hello", "Hi", 1, 5)) # Outputs one of the options.
```
---
```python
ascii_art(text)
```
Generates multiline ascii art.
Syntax:
- `text`: string, required
Example Usage:
```python
import loopypy
print(loopypy.ascii_art("Hello")) # Prints the multiline ascii text
```
---