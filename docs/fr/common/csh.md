---
layout: page
title: common/csh (français)
description: "Le shell (interprèteur de commandes) affiche une syntaxe proche de C."
content_hash: 77109f6bbf48cee909c01ee50403ae229fbd36e7
last_modified_at: 2023-09-10
related_topics:
  - title: English version
    url: /en/common/csh.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># csh

Le shell (interprèteur de commandes) affiche une syntaxe proche de C.
Voir aussi : `tcsh`.
Plus d'informations : <https://www.mkssoftware.com/docs/man1/csh.1.asp>.

- Démarrer une session interactive:

`csh`

- Démarrer une session interactive sans prendre en compte le fichier de configuration au démarrage:

`csh -f`

- Exécuter une commande:

`csh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'Exécution de la commande echo par csh'</span>`"`

- Exécuter un script:

`csh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/script.csh</span>
