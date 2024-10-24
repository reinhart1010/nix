---
layout: page
title: linux/aa-disable (polski)
description: "Wyłącz polityki bezpieczeństwa AppArmor."
content_hash: 4a81344884f3d0738e17cd1e7bece65b04a72181
last_modified_at: 2024-10-24
related_topics:
  - title: English version
    url: /en/linux/aa-disable.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aa-disable.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/aa-disable.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-disable

Wyłącz polityki bezpieczeństwa AppArmor.
Zobacz także: `aa-complain`, `aa-enforce`, `aa-status`.
Więcej informacji: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Wyłącz profile:

`sudo aa-disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/profilu1 ścieżka/do/profilu2 ...</span>

- Wyłącz profile w katalogu (domyślnie `/etc/apparmor.d`):

`sudo aa-disable --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/profili</span>
