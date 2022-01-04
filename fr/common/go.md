---
layout: page
title: common/go (français)
description: "Outil de gestion du code source Go."
content_hash: fc674df9a8e1dac46be91d36bc974e8dfda74bf5
related_topics:
  - title: English version
    url: /en/common/go.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># go

Outil de gestion du code source Go.
Certaines sous-commandes telles que `go build` ont leur propre documentation d'utilisation.
Plus d'informations : <https://golang.org>.

- Télécharger et installer un paquet, spécifié par son chemin d'importation :

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin_du_paquet</span>

- Compiler et exécuter un fichier source (il doit contenir un paquet `main`) :

`go run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>`.go`

- Compiler un fichier source dans un exécutable nommé :

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>`.go`

- Compile le paquet présent dans le répertoire courant :

`go build`

- Exécuter tous les cas de test du paquet courant (les fichiers doivent se terminer par `_test.go`) :

`go test`

- Compiler et installer le paquet actuel :

`go install`

- Initialiser un nouveau module dans le répertoire courant :

`go mod init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_module</span>
