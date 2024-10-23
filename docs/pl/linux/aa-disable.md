---
layout: page
title: linux/aa-disable (polski)
description: "Wyłącz polityki bezpieczeństwa AppArmor."
content_hash: 4a81344884f3d0738e17cd1e7bece65b04a72181
last_modified_at: 2024-10-23
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/aa-disable.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aa-disable

Wyłącz polityki bezpieczeństwa AppArmor.
Zobacz także: `aa-complain`, `aa-enforce`, `aa-status`.
Więcej informacji: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Wyłącz profile:

`sudo aa-disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/profilu1 ścieżka/do/profilu2 ...</span>

- Wyłącz profile w katalogu (domyślnie `/etc/apparmor.d`):

`sudo aa-disable --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/profili</span>
