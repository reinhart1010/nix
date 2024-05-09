---
layout: page
title: sunos/dmesg (polski)
description: "Wypisz komunikaty jądra do `stdout`."
content_hash: a83c62bb849c08ee3c2bfbbf31feb2d86599d049
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/sunos/dmesg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/dmesg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/dmesg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/dmesg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/sunos/dmesg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/dmesg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dmesg

Wypisz komunikaty jądra do `stdout`.
Więcej informacji: <https://www.unix.com/man-page/sunos/1m/dmesg>.

- Wyświetl komunikaty jądra:

`dmesg`

- Pokaż ilość pamięci fizycznej dostępnej w systemie:

`dmesg | grep -i memory`

- Wyświetl komunikaty jądra po 1 stronie naraz:

`dmesg | less`
