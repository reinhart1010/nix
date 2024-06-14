---
layout: page
title: common/bash (polski)
description: "Bourne-Again SHell, interpreter komend powłoki systemowej kompatybilny z `sh`."
content_hash: e723f4f327cb7d433aba2eea3e64160c6adc8be9
last_modified_at: 2024-06-14
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
tldri18n_status: 2
---
# bash

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

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/skryptu.sh</span>

- Wykonaj podany skrypt, wypisując wszystkie komendy przed ich wykonaniem:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/skryptu.sh</span>

- Wykonaj podany skrypt do wystąpienia pierwszego błędu:

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/skryptu.sh</span>

- Wykonaj komendy ze `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'bash jest uruchomiony'"</span>` | bash`

- Uruchom sesję w trybie [r]estrykcyjnym:

`bash -r`
