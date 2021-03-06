---
layout: page
title: common/bash (Nederlands)
description: "Bourne-Again SHell."
content_hash: af29b4e33bb9665e4ed73d9594ce5b3a7700dff7
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
---
# bash

Bourne-Again SHell.
`sh`-ondersteunende commandoregel-interpreteerder.
Meer informatie: <https://gnu.org/software/bash/>.

- Start interactieve shell:

`bash`

- Voer een commando uit:

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>`"`

- Voer commando's van bestand uit:

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand.sh</span>

- Voer commando's van bestand uit, en print alle uitgevoerde commando's naar de terminal:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand.sh</span>

- Voer commando's van bestand uit, en stop bij de eerste fout:

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand.sh</span>

- Voer commando's van stdin uit:

`bash -s`

- Print de versieinformatie van bash (gebruik `echo $BASH_VERSION` om alleen de versie te krijgen zonder licentie):

`bash --version`
