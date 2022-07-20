---
layout: page
title: linux/rpi-eeprom-update (English)
description: "Tool to update EEPROM and view other EEPROM information."
content_hash: f79fdfedf2f0b7da0ecb8084ae58e18109b36658
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rpi-eeprom-update

Tool to update EEPROM and view other EEPROM information.
More information: <https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#rpi-eeprom-update>.

- Print information about the current raspberry pi EEPROM installed:

`sudo rpi-eeprom-update`

- Update a raspberry pi EEPROM:

`sudo rpi-eeprom-update -a`

- Cancel the pending update:

`sudo rpi-eeprom-update -r`

- Display help:

`rpi-eeprom-update -h`
