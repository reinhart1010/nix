---
layout: page
title: linux/as (français)
description: "Assembleur GNU portable. Principalement destiné pour assembler la sortie de `gcc` pour être utilisé par `ld`."
content_hash: a4eff54a15d1f52fb3c6daacdc20c7681aaf87ed
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/linux/as.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/as.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/as.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/as.html
    icon: bi bi-globe
tldri18n_status: 2
---
# as

Assembleur GNU portable. Principalement destiné pour assembler la sortie de `gcc` pour être utilisé par `ld`.
Plus d'informations : <https://manned.org/as>.

- Assemble un fichier, en écrivant la sortie dans le fichier `a.out` :

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.s</span>

- Assemble la sortie vers un fichier donné :

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sortie.o</span>

- Génère la sortie plus vite en évitant le preprocess des espaces et des commentaires (doit seulement être utilisé sur des compilateurs sûrs) :

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.s</span>

- Inclut un chemin donné à la liste des répertoires dans lesquels chercher les fichiers spécifiés dans les directives `.include` :

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.s</span>
