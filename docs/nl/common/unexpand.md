---
layout: page
title: common/unexpand (Nederlands)
description: "Converteer spaties naar tabs."
content_hash: 5d618acda377c3d0fed0005e2cc862e65d0c8236
last_modified_at: 2024-06-27
related_topics:
  - title: English version
    url: /en/common/unexpand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unexpand

Converteer spaties naar tabs.
Meer informatie: <https://www.gnu.org/software/coreutils/unexpand>.

- Converteer spaties in elk bestand naar tabs en schrijf naar `stdout`:

`unexpand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Converteer spaties naar tabs en lees van `stdin`:

`unexpand`

- Converteer alle spaties, in plaats van alleen de voorloopspaties:

`unexpand -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Converteer alleen leidende reeksen van spaties (overschrijft -a):

`unexpand --first-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Plaats tabs een bepaald aantal tekens uit elkaar, niet 8 (activeert -a):

`unexpand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
