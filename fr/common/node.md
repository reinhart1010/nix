---
layout: page
title: common/node (français)
description: "Plateforme JavaScript côté serveur."
content_hash: 32112a6175c35be6f3b93ff0d4259bc896941e7f
related_topics:
  - title: Deutsch version
    url: /de/common/node.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/node.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/node.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/node.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/node.html
    icon: bi bi-globe
---
# node

Plateforme JavaScript côté serveur.
Plus d'informations : <https://nodejs.org>.

- Éxecute un fichier JavaScript :

`node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Démarre un REPL (shell interactif) :

`node`

- Évalue du code JavaScript en le passant en argument :

`node -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Évalue et affiche le résultat, très utile pour voir les versions de dépendances node :

`node -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process.versions</span>`"`

- Active l'inspecteur, mets en pause l'éxécution jusqu'à ce qu'un debugger soit connecté une fois que le code source est totalement interprété :

`node --no-lazy --inspect-brk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
