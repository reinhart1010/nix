---
layout: page
title: common/ar (français)
description: "Crée, modifie et extrais depuis des archives (`.a`, `.so`, `.o`)."
content_hash: 9a1d68b6b7d6cc355047004018a49191b7baeeb7
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/ar.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ar.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ar

Crée, modifie et extrais depuis des archives (`.a`, `.so`, `.o`).
Plus d'informations : <https://manned.org/ar>.

- E[x]trais tous les éléments depuis une archive :

`ar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive.a</span>

- Lis[t]e tous les éléments depuis une archive :

`ar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive.ar</span>

- [r]emplace ou ajoute des fichiers à une archive :

`ar r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/debian-binary chemin/vers/control.tar.gz chemin/vers/data.tar.xz ...</span>

- In[s]ère un fichier d'indexation (équivalent à `ranlib`) :

`ar s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive.a</span>

- Crée une archive avec des fichiers et un fichier d'indexation qui l'accompagne :

`ar rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1.o chemin/vers/fichier2.o ...</span>
