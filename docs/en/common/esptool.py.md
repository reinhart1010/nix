---
layout: page
title: common/esptool.py (English)
description: "Bootloader utility for Espressif chips (e.g. ESP8266)."
content_hash: 392c9100861072aa34389b55da1cbfc9635fe28e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# esptool.py

Bootloader utility for Espressif chips (e.g. ESP8266).
More information: <https://docs.espressif.com/projects/esptool/en/latest/esp32/>.

- Flash a firmware file to an ESP chip with a given port and baud rate:

`sudo esptool.py --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">baud_rate</span>` write_flash 0x0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/firmware.bin</span>

- Clear the flash of an ESP chip:

`sudo esptool.py --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">baud_rate</span>` erase_flash`
