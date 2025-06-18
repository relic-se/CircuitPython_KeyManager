# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2024 Cooper Dalrymple
#
# SPDX-License-Identifier: Unlicense

import asyncio

import board
from keypad import Keys

from relic_keymanager import Keyboard

keyboard = Keyboard(
    keys=Keys((board.USER_SW,), value_when_pressed=False, pull=False),
)

keyboard.on_voice_press = lambda voice: print(f"Pressed: {voice.note.notenum:d}")
keyboard.on_voice_release = lambda voice: print(f"Released: {voice.note.notenum:d}")

asyncio.run(keyboard.update())
