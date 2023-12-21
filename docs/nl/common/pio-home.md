---
layout: page
title: common/pio-home (Nederlands)
description: "Lanceer de PlatformIO Home web server."
content_hash: 8f25019e9e49bdf8ac0e73ffa87543921474c3fd
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-home.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio home

Lanceer de PlatformIO Home web server.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>.

- Open PlatformIO Home in de standaard web browser:

`pio home`

- Gebruik een specifieke HTTP poort (standaard 8008):

`pio home --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>

- Koppel aan een specifiek IP adres (standaard 127.0.0.1):

`pio home --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adres</span>

- Open niet automatisch PlatformIO Home in de standaard web browser:

`pio home --no-open`

- Sluit de server af na n (in seconden) als er niemand verbonden is:

`pio home --shutdown-timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Specificeer een unieke sessie identificatie om PlatformIO Home geïsoleerd te houden van andere instances en beschermd van toegang van derde partijen:

`pio home --session-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>
