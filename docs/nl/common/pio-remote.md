---
layout: page
title: common/pio-remote (Nederlands)
description: "Helper commando voor PlatformIO Remote Development."
content_hash: f47251e8fc4be878e438db89b46e589a208ef433
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-remote.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio remote

Helper commando voor PlatformIO Remote Development.
`pio remote [commando]` accepteert dezelfde argumenten als de lokale tegenhanger `pio [commando]`.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/remote/index.html>.

- Toon alle actieve Remote Agents:

`pio remote agent list`

- Start een nieuwe Remote Agent met een specifieke naam en deel deze met vrienden:

`pio remote agent start --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_naam</span>` --share `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example1@example.com</span>` --share `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example2@example.com</span>

- Toon alle apparaten van een specifieke Agents (laat `--agent` weg voor alle Agents):

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_naam1</span>` --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_naam2</span>` device list`

- Verbind met een seriele poort van een remote apparaat:

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_naam</span>` device monitor`

- Voer alle doelen uit op een gespecificeerde Agent:

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_naam</span>` run`

- Update geïnstalleerde kern pakketten, ontwikkelplatformen en globale bibliotheken op een specifieke Agent:

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_naam</span>` update`

- Voer alle testen uit in alle omgevingen op een specifieke Agent:

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agent_naam</span>` test`
