---
layout: page
title: common/pio-check (Nederlands)
description: "Voer een statische analyse check uit op een PlatformIO project."
content_hash: 4c703bccd19cc5d8e8dcd6f5ed2db23aee305807
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-check.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio check

Voer een statische analyse check uit op een PlatformIO project.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_check.html>.

- Voer een basis analyse check uit op het huidige project:

`pio check`

- Voer een basis analyse check uit op een specifiek project:

`pio check --project-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_map</span>

- Voer een analyse check uit voor een specifieke omgeving:

`pio check --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">omgeving</span>

- Voer een analyse check uit en rapporteer alleen een specifiek niveau:

`pio check --severity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">low|medium|high</span>

- Voer een analyse check uit en toon gedetailleerde informatie bij het verwerken van omgevingen:

`pio check --verbose`
