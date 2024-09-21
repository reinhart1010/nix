---
layout: page
title: linux/pwd (Nederlands)
description: "Print de naam van de huidige/werkdirectory."
content_hash: 862e14364505e9ced854ecfb05556fead4d8d5cd
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/linux/pwd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pwd.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/linux/pwd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pwd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/pwd.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pwd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pwd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pwd

Print de naam van de huidige/werkdirectory.
Meer informatie: <https://www.gnu.org/software/coreutils/pwd>.

- Print de huidige directory:

`pwd`

- Print de huidige directory en los alle symlinks op (d.w.z. toon het "fysieke" pad):

`pwd --physical`

- Print de huidige logische directory:

`pwd --logical`
