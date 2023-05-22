---
layout: page
title: common/apg (français)
description: "Crée arbitrairement les mots de passe aléatoires et complexes."
content_hash: d6b14a7adc6d8b8ac3011063cf879d59158447a9
last_modified_at: 2023-05-22
related_topics:
  - title: English version
    url: /en/common/apg.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/apg.html
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
# apg

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

`apg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_dictionnaire</span>
