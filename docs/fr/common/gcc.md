---
layout: page
title: common/gcc (français)
description: "Préprocesse et compile des fichiers sources C et C++, pour ensuite les assembler et les lier entre eux."
content_hash: 7ebf16bf348ccf130ebe60caf2da257516056b28
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/gcc.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gcc.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/gcc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gcc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/gcc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcc

Préprocesse et compile des fichiers sources C et C++, pour ensuite les assembler et les lier entre eux.
Plus d'informations : <https://gcc.gnu.org>.

- Compile plusieurs fichiers source en un exécutable :

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichier1.c chemin/vers/le/fichier2.c ...</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/l'exécutable/à/produire</span>

- Active les averissements et les symboles de débogage dans la sortie de commande :

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichiersource.c</span>` -Wall -Og -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/l'exécutable/à/produire</span>

- Inclut les bibliothèques depuis un chemin différent de celui par défaut :

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichiersource.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/l'exécutable/à/produire</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/les/fichiers/d'en-tête</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/la/bibliothèque</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bibliothèque</span>

- Compile le code source en des instructions d'assemblage :

`gcc -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichiersource.c</span>

- Compile le code source en un fichier objet sans le lier :

`gcc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/fichiersource.c</span>
