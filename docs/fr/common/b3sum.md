---
layout: page
title: common/b3sum (français)
description: "Calcule les sommes de contrôle cryptographiques BLAKE3."
content_hash: cf8f7927268d14d264f9eafa19abd057cb3c72e9
last_modified_at: 2024-03-07
related_topics:
  - title: English version
    url: /en/common/b3sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# b3sum

Calcule les sommes de contrôle cryptographiques BLAKE3.
Plus d'informations : <https://github.com/BLAKE3-team/BLAKE3/tree/master/b3sum>.

- Calcule la somme de contrôle BLAKE3 pour un ou plusieurs fichiers :

`b3sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1 chemin/vers/fichier2 ...</span>

- Calcule et enregistre la liste des sommes de contrôle BLAKE3 dans un fichier :

`b3sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1 chemin/vers/fichier2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.b3</span>

- Calculer une somme de contrôle BLAKE3 à partir de `stdin` :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>` | b3sum`

- Lit un fichier de sommes et de noms de fichiers BLAKE3 et vérifie que tous les fichiers ont des sommes de contrôle correspondantes :

`b3sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.b3</span>

- N'affiche un message que pour les fichiers manquants ou en cas d'échec de la vérification :

`b3sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.b3</span>
