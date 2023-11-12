---
layout: page
title: linux/apx-subsystems (Nederlands)
description: "Beheer subsystemen in `apx`."
content_hash: bf47743d7a7851f2d7b9342ac4beae1504703708
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/apx-subsystems.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apx subsystems

Beheer subsystemen in `apx`.
Subsystemen zijn containers die kunnen worden gemaakt op basis van reeds bestaande stapels.
Meer informatie: <https://github.com/Vanilla-OS/apx>.

- Maak interactief een nieuw subsysteem:

`apx subsystems new`

- Toon alle beschikbare subsystemen:

`apx subsystems list`

- Reset een specifiek subsysteem naar zijn initiële toestand:

`apx subsystems reset --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- [f]orceer een reset van een specifiek subsysteem:

`apx subsystems reset --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` --force`

- Verwijder een specifiek subsysteem:

`apx subsystems rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- [f]orceer het verwijderen van een specifiek subsysteem:

`apx subsystems rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` --force`
