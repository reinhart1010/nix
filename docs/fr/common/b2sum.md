---
layout: page
title: common/b2sum (français)
description: "Calcule les sommes de contrôle cryptographiques BLAKE2."
content_hash: 8ef360d34862f315a2a0ff411d812220bbd122a0
last_modified_at: 2023-07-03
related_topics:
  - title: English version
    url: /en/common/b2sum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/b2sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/b2sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/b2sum.html
    icon: bi bi-globe
---
# b2sum

Calcule les sommes de contrôle cryptographiques BLAKE2.
Plus d'informations : <https://www.gnu.org/software/coreutils/b2sum>.

- Calcule la somme de contrôle BLAKE2 d'un fichier :

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Calcule les sommes de contrôle BLAKE2 pour plusieurs fichiers :

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier2</span>

- Calcule la somme de contrôle BLAKE2 depuis `stdin` :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>` | b2sum`

- Lis un fichier contenant des sommes de contrôle BLAKE2 et des noms de fichier et vérifie que tous les fichiers ont des sommes de contrôle correspondantes :

`b2sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.b2</span>

- Affiche un message uniquement pour les fichiers manquants ou lorsque la vérification échoue :

`b2sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.b2</span>

- N'affiche un message que pour les fichiers pour lesquels la vérification a échoué, en ignorant les fichiers manquants :

`b2sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.b2</span>
