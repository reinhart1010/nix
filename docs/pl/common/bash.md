---
layout: page
title: common/bash (polski)
description: "Bourne-Again SHell, interpreter komend powłoki systemowej kompatybilny z `sh`."
content_hash: a7a0fcdeafcea16c1e0994d4094a5a99b65817e7
last_modified_at: 2024-04-18
related_topics:
  - title: Deutsch version
    url: /de/common/bash.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bash.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bash.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bash.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bash.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bash.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bash.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/bash.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bash.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bash

Bourne-Again SHell, interpreter komend powłoki systemowej kompatybilny z `sh`.
Zobacz także: `zsh`, `histexpand`.
Więcej informacji: <https://www.gnu.org/software/bash/>.

- Rozpocznij interaktywną sesję powłoki:

`bash`

- Rozpocznij interaktywną sesję powłoki bez ładowania konfiguracji:

`bash --norc`

- Wywołaj określone komendy:

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'bash jest uruchomiony'</span>`"`

- Uruchom podany skrypt:

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scieżka/do/skryptu.sh</span>

- Wykonaj podany skrypt, wypisując wszystkie komendy przed ich wykonaniem:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scieżka/do/skryptu.sh</span>

- Wykonaj podany skrypt do wystąpienia pierwszego błędu:

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scieżka/do/skryptu.sh</span>

- Wykonaj komendy ze `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'bash jest uruchomiony'"</span>` | bash`

- Uruchom sesję w trybie [r]estrykcyjnym:

`bash -r`
