---
layout: page
title: linux/vcgencmd (English)
description: "Print system information for a Raspberry Pi."
content_hash: af6b8d8a03611461bada4b30e79c68ce17b5ed93
---
# vcgencmd

Print system information for a Raspberry Pi.
More information: <https://www.raspberrypi.org/documentation/raspbian/applications/vcgencmd.md>.

- List all available commands:

`vcgencmd commands`

- Print the current CPU temperature:

`vcgencmd measure_temp`

- Print the current voltage:

`vcgencmd measure_volts`

- Print the throttled state of the system as a bit pattern:

`vcgencmd get_throttled`

- Print the bootloader config (only available on Raspberry Pi 4 models):

`vcgencmd bootloader_config`

- Display Help:

`vcgencmd --help`
