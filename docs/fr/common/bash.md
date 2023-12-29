---
layout: page
title: common/bash (français)
description: "Bourne-Again SHell, un interpréteur de ligne de commande compatible avec `sh`."
content_hash: 854be89d069afc2ce2ea8cef0e1d35da7dd3d5b8
last_modified_at: 2023-12-29
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bash

Bourne-Again SHell, un interpréteur de ligne de commande compatible avec `sh`.
Voir aussi `histexpand` pour l'expansion de l'historique.
Plus d'informations : <https://www.gnu.org/software/bash/>.

- Démarre une session shell interactive :

`bash`

- Exécute une commande, puis termine la session :

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>`"`

- Exécute un script :

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/script.sh</span>

- Exécute un script en affichant chaque commande avant de l'exécuter :

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/script.sh</span>

- Exécute un script en s'arrêtant à la première erreur :

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/script.sh</span>

- Lit et exécute des commandes depuis l'entrée standard `stdin` :

`bash -s`

- Affiche la version de Bash (`$BASH_VERSION` ne contenant que la version, sans les informations de license):

`bash --version`
