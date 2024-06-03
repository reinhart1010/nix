---
layout: page
title: common/rsync (français)
description: "Transférer des fichiers vers ou depuis un hôte distant (pas entre deux hôtes distants)."
content_hash: 072e814530087947b5640df2b5a4f76004d9aad1
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/rsync.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rsync.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rsync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rsync.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rsync.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rsync.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rsync

Transférer des fichiers vers ou depuis un hôte distant (pas entre deux hôtes distants).
Peut transférer un ou plusieurs fichiers correspondant à un motif.
Plus d'informations : <https://download.samba.org/pub/rsync/rsync.1>.

- Transfère un fichier :

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/origine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/destination</span>

- Utilise le mode archive (copier récursivement les répertoires, copier les liens symboliques sans résolution et conserver les autorisations, la propriété et les délais de modification) :

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--archive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/origine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/destination</span>

- Transférer le contenu d'un dossier :

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/origine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/destination</span>

- Transférer le contenu d'un dossier (mais pas le dossier lui-même) :

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/origine</span>`/ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/destination</span>

- Utiliser le mode archive, résolvant les liens symboliques et ignorant les fichiers déjà transférés sauf si plus récents :

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-auL|--archive --update --copy-links</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/origine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/destination</span>

- Transférer un fichier vers un hôte distant exécutant `rsyncd` et supprimez les fichiers sur la destination qui n'existent pas sur l'hôte distant :

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` --delete rsync://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/origine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/destination</span>

- Transférer un fichier par SSH et afficher l'avancement global du transfert :

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--rsh</span>` 'ssh -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>`' --info=progress2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/origine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/destination</span>
