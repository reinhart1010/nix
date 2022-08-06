---
layout: page
title: common/apg (français)
description: "Crée arbitrairement les mots de passe aléatoires et complexes."
content_hash: 05999b3408f358167dc03dcfb7205d8bfe12e4f4
related_topics:
  - title: English version
    url: /en/common/apg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/apg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/apg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/apg.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apg

Crée arbitrairement les mots de passe aléatoires et complexes.
Plus d'informations : <https://manned.org/apg>.

- Crée des mots de passe aléatoires (la longueur par défaut est 8) :

`apg`

- Crée un mot de passe avec au moins 1 symbole (S), 1 Nombre (N), 1 Majuscule (C), 1 Minuscule (L) :

`apg -M SNCL`

- Crée un mot de passe avec 16 caractères :

`apg -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Crée un mot de passe avec une longeur maximum de 16 :

`apg -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Crée un mot de passe qui n'apparaît pas dans le dictionnaire (le fichier de dictionnaire doit être donné) :

`apg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_dictionnaire</span>
