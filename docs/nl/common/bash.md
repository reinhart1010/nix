---
layout: page
title: common/bash (Nederlands)
description: "Bourne-Again SHell, `sh`-ondersteunende commandoregel-interpreteerder."
content_hash: 46f429de9af0aa44dd12a8bc6a245775729225c3
last_modified_at: 2023-11-12
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

Bourne-Again SHell, `sh`-ondersteunende commandoregel-interpreteerder.
Bekijk ook: `zsh`, `histexpand` (history expansion).
Meer informatie: <https://gnu.org/software/bash/>.

- Start een interactieve shell sessie:

`bash`

- Start een interactieve shell sessie zonder het laden van startup configuratie:

`bash --norc`

- Voer een [c]ommando uit:

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'bash is executed'</span>`"`

- Voer commando's van bestand uit:

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.sh</span>

- Voer commando's van bestand uit, en print alle uitgevoerde commando's naar de terminal:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.sh</span>

- Voer commando's van bestand uit, en stop bij de eerste fout:

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.sh</span>

- Voer commando's van `stdin` uit:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'bash is executed'"</span>` | bash`

- Start een beperkte shell sessie:

`bash -r`
