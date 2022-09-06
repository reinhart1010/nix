---
layout: page
title: linux/man (français)
description: "Interface de consultation des pages du manuel de référence."
content_hash: 6dc8b5b20883ec42976748c6ee20d2082da16dba
related_topics:
  - title: English version
    url: /en/linux/man.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># man

Interface de consultation des pages du manuel de référence.
Plus d'informations : <https://www.man7.org/linux/man-pages/man1/man.1.html>.

- Affiche la page de manuel d'une commande :

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Affiche la page de manuel de la section 7 d'une commande :

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Liste toutes les sections dans lesquelles se trouve une commande :

`man --whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Affiche tous les chemins où se trouvent les pages de manuel :

`man --path`

- Affiche l'emplacement d'une page de manuel plutôt que la page elle-même :

`man --where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Affiche la page de manuel dans une langue particulière :

`man --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fr_FR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Cherche toutes les pages de manuel contenant la chaîne de caractères spécifée :

`man --apropos "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_de_caractères</span>`"`
