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
|Name|Description|
|----|-----------|
|`setApiKey(key)`|Sets the API key for automated gathering later on.|
|`getApiKey()`|Returns the API key|
|`ai(prompt, speed)`|Uses the /openai/text endpoint to generate text from ChatGPT.|
|`owoify(text)`|Owoifies the text and returns it|
|`emojify(text)`|Turns the text into regional indicators in Discord format.|
|`qr(data)`|Turns the given data into a QR code and returns the image buffer.|
|`currency(base, target, amount)`|Converts  one currency to another.|
|`seconds_to_time(seconds)`|Converts given seconds into formatted time (HH\:MM:SS)|
|`pick(*args)`|Picks an option off of the given ones.|
|`ascii_art(text)`|Returns multiline ascii art off of the given text.|
|`Coming Soon`|More functions are coming soon.|

Usages:
---
```python
setApiKey(key)
```
Sets the API key for later use. Required for most endpoints.
Syntax:
- `key`: string, required
---
```python
getApiKey()
```
Retrieves and returns the current API key.

---
```python
ai(prompt, speed)
```
Uses the /openai/text endpoint to generate text from ChatGPT.
Syntax:
- `prompt`: String, required
- `speed`: Integer, optional, defaults to 1. (0: large, 1: balanced, 2: fast)
---
```python
owoify(text)
```
Owoifies the text and returns it.
Syntax:
- `text`: string, required
---
```python
emojify(text)
```
Turns the text into regional indicators in Discord format.
Syntax:
- `text` string, required
---
```python
qr(data)
```
Turns the given data into a QR code and returns the image buffer.
Syntax:
- `data`: string, required
---
```python
currency(base, target, amount)
```
Converts  one currency to another.
Syntax:
- `base`: string, required
- `target`: string, required
- `amount`: integer, required
---
```python
seconds_to_time(seconds)
```
Converts given seconds into formatted time (HH\:MM:SS)
Syntax:
- `seconds` integer, required
---
more docs tomorrow
