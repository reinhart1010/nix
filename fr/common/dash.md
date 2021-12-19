---
layout: page
title: common/dash (français)
description: "Debian Almquist SHell, une implémentation de `sh` moderne, conforme à POSIX (non compatible avec Bash)."
content_hash: 7e09aa3b5a9115735e13e4f587a511430da532ec
related_topics:
  - title: English version
    url: /en/common/dash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dash.html
    icon: bi bi-globe
---
# dash

Debian Almquist SHell, une implémentation de `sh` moderne, conforme à POSIX (non compatible avec Bash).
Plus d'informations : <https://manned.org/dash>.

- Démarre une session shell interactive :

`dash`

- Exécute une commande, puis termine la session :

`dash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>`"`

- Exécute un script :

`dash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/script.sh</span>

- Exécute un script en affichant chaque commande avant de l'exécuter :

`dash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/script.sh</span>

- Exécute un script en s'arrêtant à la première erreur :

`dash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/script.sh</span>

- Lit et exécute des commandes depuis l'entrée standard `stdin` :

`dash -s`
