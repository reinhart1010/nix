---
layout: page
title: common/ln (français)
description: "Crée des liens vers des fichiers et répertoires."
content_hash: 39a4fb3c5ef3a4c97f8868fbaccdb9ccfe6e375e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ln.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ln.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ln.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ln.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ln.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ln.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ln.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ln

Crée des liens vers des fichiers et répertoires.
Plus d'informations : <https://www.gnu.org/software/coreutils/ln>.

- Crée un lien symbolique vers un fichier ou un répertoire :

`ln -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/fichier_ou_repertoire</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/lien_symbolique</span>

- Modifie la cible d'un lien symbolique existant :

`ln -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/nouveau_fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/lien_symbolique</span>

- Crée un lien dur vers un fichier :

`ln `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/lien_dur</span>
