---
layout: page
title: linux/vcgencmd (English)
description: "Print system information for a Raspberry Pi."
content_hash: da365194fc6819fd6edc1b6f11f96784d3db7c65
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# vcgencmd

Print system information for a Raspberry Pi.
More information: <https://www.raspberrypi.org/documentation/computers/os.html#vcgencmd>.

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
