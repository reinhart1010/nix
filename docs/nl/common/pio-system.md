---
layout: page
title: common/pio-system (Nederlands)
description: "Gemengde systeem commando's voor PlatformIO."
content_hash: 06104c4b9b4941cba581073d95eefcf7a3f5bcc5
last_modified_at: 2024-03-10
related_topics:
  - title: English version
    url: /en/common/pio-system.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio system

Gemengde systeem commando's voor PlatformIO.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/system/>.

- Installeer shell completion voor de huidige shell (ondersteund Bash, fish, Zsh en PowerShell):

`pio system completion install`

- Deinstalleer shell completion voor de huidige shell:

`pio system completion uninstall`

- Toon systeem-wijde PlatformIO informatie:

`pio system info`

- Verwijder ongebruikte PlatformIO data:

`pio system prune`

- Verwijder alleen gecachte data:

`pio system prune --cache`

- Toon ongebruikte PlatformIO data die verwijderd zou worden, maar verwijder het niet echt:

`pio system prune --dry-run`
