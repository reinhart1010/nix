---
layout: page
title: linux/aa-status (Nederlands)
description: "Toon de momenteel geladen AppArmor-modules."
content_hash: d55a8ac24ae32f02144aeeed1b5c9d0b2b24c4b9
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/linux/aa-status.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-status

Toon de momenteel geladen AppArmor-modules.
Bekijk ook: `aa-complain`, `aa-disable`, `aa-enforce`.
Meer informatie: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>.

- Controleer de status:

`sudo aa-status`

- Toon het aantal geladen profielen:

`sudo aa-status --profiled`

- Toon het aantal geladen afdwingende profielen:

`sudo aa-status --enforced`

- Toon het aantal geladen niet-afdwingende profielen:

`sudo aa-status --complaining`

- Toon het aantal geladen afdwingende profielen die taken beëindigen:

`sudo aa-status --kill`
