---
layout: page
title: linux/apx-stacks (Nederlands)
description: "Beheer stacks in `apx`."
content_hash: 698da9b6dfc5c4c12a75a84e455ddccc57584286
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/apx-stacks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apx stacks

Beheer stacks in `apx`.
Let op: Door gebruikers gecreëerde pakketbeheerderconfiguraties worden opgeslagen in `~/.local/share/apx/pkgmanagers`.
Meer informatie: <https://github.com/Vanilla-OS/apx>.

- Maak interactief een nieuwe stack configuratie:

`apx stacks new`

- Update interactief een nieuwe stack configuratie:

`apx stacks update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Toon alle beschikbare stack configuraties:

`apx stacks list`

- Verwijder een specifieke stack configuratie:

`apx stacks rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Importeer een stack configuratie:

`apx stacks import --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/stack.yml</span>

- Exporteer de stack configuratie (Let op: de output flag is optioneel, het wordt standaard geëxporteerd naar de huidige map):

`apx stacks export --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/output_bestand</span>
