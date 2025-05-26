<p align="center">
  <a href="https://api.loopy5418.dev/">
    <img width="200" src="https://cdn.discordapp.com/icons/1365258638222164008/b0ac96e1df99c594cfd6ccb5d435f618.webp" alt="loopy-ts">
  </a>
</p>

<div align="center">
  <b>The official python wrapper for api.loopy5418.dev.</b>
</div>

---

<br/>

<div align="center">

[![Loopy Server][loopy-ts-server]][loopy-ts-server-url] &nbsp; &nbsp;
![Website](https://img.shields.io/website?url=https%3A%2F%2Fapi.loopy5418.dev%2F&label=api.loopy5418.dev) &nbsp; &nbsp;

[loopy-ts-server]: https://img.shields.io/discord/1365258638222164008?color=5865F2&logo=discord&logoColor=white

[loopy-ts-server-url]: https://discord.gg/ZwK2W7GxhA

  </div>

<br />

<div align = "center">

**[ Documentation ](https://api.loopy5418.dev/)** | **[ Support Server ](https://discord.gg/ZwK2W7GxhA)** | **[ PyPi ](https://pypi.org/project/loopypy/)** | **[ GitHub ](https://github.com/api-loopy5418-dev/loopypy)**

</div>

---

## About

loopy-py is a wrapper for api.loopy5418.dev made in Python.

It's easy for people that don't know how to make HTTP requests.

## Setup

First install the package with 
```bash
pip install loopypy
```

Then paste this into you app.py (or whatever you call it!)
```python
import loopypy
# Or you can just do 
# from 'loopypy' import setApiKey, getApiKey, ai

loopypy.setApiKey("Secret!")
# You can get your api key at our server
# https://discord.gg/ZwK2W7GxhA


# Open AI
ask = loopy.ai("Hello, how are you! What's the weather in New York?")
print(ask.response)

# After running check your terminal!
# It should say something like:
# "Hello! I'm just a program, so I 
# don't have feelings, but I'm here to help you. 
# I don't have real-time data on the weather. 
# For the most accurate and current weather 
# information in New York, please check a 
# reliable weather website or app."
```


<details>
  <summary><h3>Function List</h3></summary>

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
 </summary>
</details>