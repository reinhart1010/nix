---
layout: page
title: linux/aa-status (polski)
description: "Wyświetl aktualnie załadowane moduły AppArmor."
content_hash: bf7fe11ac96fc2a56997b796bcbb1f20b9b17767
last_modified_at: 2024-10-24
related_topics:
  - title: English version
    url: /en/linux/aa-status.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/aa-status.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-status

Wyświetl aktualnie załadowane moduły AppArmor.
Zobacz także: `aa-complain`, `aa-disable`, `aa-enforce`.
Więcej informacji: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>.

- Sprawdź status:

`sudo aa-status`

- Wyświetl liczbę załadowanych polityk:

`sudo aa-status --profiled`

- Wyświetl liczbę aktualnie załadowanych wymuszonych polityk:

`sudo aa-status --enforced`

- Wyświetl liczbę załadowanych niewymuszonych polityk:

`sudo aa-status --complaining`

- Wyświetl liczbę załadowanych wymuszonych polityk, które zabijają zadania:

`sudo aa-status --kill`
