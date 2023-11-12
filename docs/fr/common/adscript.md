---
layout: page
title: common/adscript (français)
description: "Compilateur pour fichiers Adscript."
content_hash: 1914c6e6dea0aa9a2f530a25f9c7b6c8bf985d5a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/adscript.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/adscript.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adscript.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adscript.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adscript.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adscript

Compilateur pour fichiers Adscript.
Plus d'informations : <https://github.com/Amplus2/Adscript>.

- Compile un fichier vers un fichier objet :

`adscript --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_source.adscript</span>

- Compile et lie un fichier vers un exécutable autonome :

`adscript --executable --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_source.adscript</span>

- Compile un fichier vers LLVM IR à la place du code machine natif :

`adscript --llvm-ir --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.ll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_source.adscript</span>

- Fait une compilation croisée d'un fichier vers un fichier objet pour une architecture CPU ou un système d'exploitation distant :

`adscript --target-triple `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i386-linux-elf</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_source.adscript</span>
