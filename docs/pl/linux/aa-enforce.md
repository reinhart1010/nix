---
layout: page
title: linux/aa-enforce (polski)
description: "Ustaw profil AppArmor w tryb wymuszony."
content_hash: ca0aa4ff154d64554be73de92ccb1397a3e8217f
last_modified_at: 2024-10-24
related_topics:
  - title: English version
    url: /en/linux/aa-enforce.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/aa-enforce.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-enforce

Ustaw profil AppArmor w tryb wymuszony.
Zobacz także: `aa-complain`, `aa-disable`, `aa-status`.
Więcej informacji: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>.

- Włącz profil:

`sudo aa-enforce --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/profilu</span>

- Włącz profile:

`sudo aa-enforce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/profilu1 ścieżka/do/profilu2 ...</span>
