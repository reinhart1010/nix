---
layout: page
title: common/pio-run (Nederlands)
description: "Voer PlatformIO project doelen uit."
content_hash: 184a64182454871e215a982bdb16051d7302645d
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio run

Voer PlatformIO project doelen uit.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_run.html>.

- Toon alle beschikbare project doelen:

`pio run --list-targets`

- Toon alle beschikbare project doelen voor een specifieke omgeving:

`pio run --list-targets --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">omgeving</span>

- Voer alle doelen uit:

`pio run`

- Voer alle doelen uit voor de gespecificeerde omgevingen:

`pio run --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">omgeving1</span>` --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">omgeving2</span>

- Voer gespecificeerde doelen uit:

`pio run --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel1</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel2</span>

- Voer de doelen uit van een specifiek configuratiebestand:

`pio run --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/platformio.ini</span>
