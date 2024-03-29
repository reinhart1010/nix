---
layout: page
title: common/ksh (français)
description: "Korn SHell, un interpréteur de ligne de commande compatible avec Bash."
content_hash: cfde920e42162b7e50a739073137f0c4e6e92a0a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ksh.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ksh

Korn SHell, un interpréteur de ligne de commande compatible avec Bash.
Voir aussi `histexpand` pour l'expansion de l'historique.
Plus d'informations : <http://kornshell.com>.

- Démarre une session shell interactive :

`ksh`

- Exécute une commande, puis termine la session :

`ksh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>`"`

- Exécute un script :

`ksh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/script.ksh</span>

- Exécute un script en affichant chaque commande avant de l'exécuter :

`ksh -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/script.ksh</span>
