---
layout: page
title: common/rsync (français)
description: "Transférer des fichiers vers ou depuis un hôte distant (pas entre deux hôtes distants)."
content_hash: fae0a79421ac9a9917693549ba3bffaaf67ac967
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# rsync

Transférer des fichiers vers ou depuis un hôte distant (pas entre deux hôtes distants).
Peut transférer un ou plusieurs fichiers correspondant à un motif.
Plus d'informations : <https://download.samba.org/pub/rsync/rsync.1>.

- Transférer un fichier local vers un serveur distant :

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_local</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_distant</span>

- Transférer un fichier d'un serveur distant vers l'hôte local :

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_local</span>

- Transférer un fichier sous forme d'[a]rchive (pour conserver les attributs) et compressé ([z]ippé), en mode [v]erbeux, lisible par l'[h]umain et afficher la [p]rogression du transfert :

`rsync -azvhP `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_local</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_distant</span>

- Transférer un dossier et tous ses sous-dossiers d'un hôte distant vers l'hôte local :

`rsync -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_local</span>

- Transférer le contenu d'un dossier (mais pas le dossier lui-même) d'un hôte distant vers un hôte local :

`rsync -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_distant</span>`/ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_local</span>

- Transférer un dossier [r]écursivement, dans une [a]rchive pour conserver les attributs, en résolvant les [l]iens symboliques, et ignorant les fichiers déjà transférés sa[u]f si plus récents :

`rsync -rauL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_local</span>

- Transférer un fichier par SSH et effacer les fichiers de l'hôte local qui n'existent pas sur l'hôte distant :

`rsync -e ssh --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_local</span>

- Transférer un fichier par SSH et afficher l'avancement global du transfert :

`rsync -e ssh --info=progress2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_local</span>
