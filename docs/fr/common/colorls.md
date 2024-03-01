---
layout: page
title: common/colorls (français)
description: "Embellit la sortie de la commande `ls`, avec des icônes coloreés ou provenant de font-awesome. Disponible sous forme de gemme Ruby."
content_hash: 4a9645a38b40decbe94f113b0b44403430395a15
last_modified_at: 2024-03-01
related_topics:
  - title: English version
    url: /en/common/colorls.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/colorls.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/colorls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># colorls

Embellit la sortie de la commande `ls`, avec des icônes coloreés ou provenant de font-awesome. Disponible sous forme de gemme Ruby.
Plus d'informations : <https://github.com/athityakumar/colorls>.

- Liste les fichiers, un par ligne :

`colorls -1`

- Liste tous les fichiers, y compris les fichiers cachés :

`colorls --all`

- Liste au format long (autorisations, propriété, taille et date de modification) de tous les fichiers :

`colorls --long --all`

- Ne liste que les répertoires :

`colorls --dirs`
