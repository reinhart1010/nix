---
layout: page
title: common/pio-device (Nederlands)
description: "Beheer en monitor PlatformIO apparaten."
content_hash: 63d701c42256ba8f7e408ce6e32522e95a9810f0
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/pio-device.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio device

Beheer en monitor PlatformIO apparaten.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/device/>.

- Toon alle beschikbare seriele poorten:

`pio device list`

- Toon alle beschikbare logische apparaten:

`pio device list --logical`

- Start een interactieve apparaat monitor:

`pio device monitor`

- Start een interactieve apparaat monitor en luister naar een specifieke poort:

`pio device monitor --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSBX</span>

- Start een interactieve apparaat monitor en stel een specifieke baud in (standaard is 9600):

`pio device monitor --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">57600</span>

- Start een interactieve apparaat monitor en stel een specifieke EOL karakter in (standaard is `CRLF`):

`pio device monitor --eol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CRLF|CR|LF</span>

- Ga naar het menu van de interactieve apparaat monitor:

`<Ctrl> + T`
