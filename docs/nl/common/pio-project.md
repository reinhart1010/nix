---
layout: page
title: common/pio-project (Nederlands)
description: "Tool voor het beheren van PlatformIO projecten."
content_hash: 2327517a165b1afefff706aa4f07b452b1be6bce
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-project.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio project

Tool voor het beheren van PlatformIO projecten.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/project/>.

- Initialiseer een nieuw PlatformIO project:

`pio project init`

- Initialiseer een nieuw PlatformIO project in een specifieke map:

`pio project init --project-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/project_map</span>

- Initialiseer een nieuw PlatformIO project, met een gespecificeerd board ID:

`pio project init --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ATmega328P|uno|...</span>

- Initialiseer een nieuw PlatformIO gebaseerd project, met een of meerdere gespecificeerde project opties:

`pio project init --project-option="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optie</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>`" --project-option="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optie</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>`"`

- Toon de configuratie van een project:

`pio project config`
