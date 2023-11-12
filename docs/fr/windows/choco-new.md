---
layout: page
title: windows/choco-new (français)
description: "Générez de nouveaux fichiers de spécifications de package avec Chocolatey."
content_hash: f358f582c7fa463d770e49ad6bc9af8060422acc
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-new.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-new.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-new.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-new.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-new.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco new

Générez de nouveaux fichiers de spécifications de package avec Chocolatey.
Plus d'informations : <https://chocolatey.org/docs/commands-new>.

- Créer un nouveau squelette de package :

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Créer un nouveau package avec une version spécifique :

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Créer un nouveau package avec un nom de responsable spécifique :

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>` --maintainer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_mainteneur</span>

- Créer un nouveau package dans un répertoire de sortie personnalisé :

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>` --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>

- Créez un nouveau package avec des URL d'installation 32 bits et 64 bits spécifiques :

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>` url="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`" url64="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`
