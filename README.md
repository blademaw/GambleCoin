# GambleCoin.py

A game (or almost game) about betting and gambling coins.

## Description

Currently running on Python 2.7 with module Tkinter (not tkinter, for python3). Lots of bugs need fixing. Game is also really lacking in terms of UX and depth. Working on it...

An example of some outputted code:
```
Coinflip Result: 0
Coinflip Result: Loss
Item Effect: +25% Bonus from Loss
Total Coins without Multiplier: 45
Total Coins after Multiplier & Final: 47.25
```

## Built With

* [Python 2.7](https://www.python.org/downloads/) - Language Used
* [Tkinter](https://wiki.python.org/moin/TkInter) - Module Used for GUI

# Changelog

### Version 1.0.1
- Added titles to windows
- Added restart & quit buttons
- Fixed a bug where user couldn't purchase upgrade due to already owning it even though user didn't own upgrade
- Fixed labels and added flair

### Version 1.0.2
- Added AutoRoll feature
	* Allows user to gamble x amount of times
	* Only prints output in console at the moment
- Converted AutoRoll from `.pack()` to `.grid()`
- Converted main display from `.pack()` to `grid()` (still working on it)
