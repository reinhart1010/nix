---
layout: page
title: linux/aa-enforce (polski)
description: "Ustaw profil AppArmor w tryb wymuszony."
content_hash: ca0aa4ff154d64554be73de92ccb1397a3e8217f
last_modified_at: 2024-10-23
related_topics:
  - title: English version
    url: /en/linux/aa-enforce.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/aa-enforce.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/aa-enforce.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aa-enforce

Ustaw profil AppArmor w tryb wymuszony.
Zobacz także: `aa-complain`, `aa-disable`, `aa-status`.
Więcej informacji: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>.

- Włącz profil:

`sudo aa-enforce --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/profilu</span>

- Włącz profile:

`sudo aa-enforce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/profilu1 ścieżka/do/profilu2 ...</span>
