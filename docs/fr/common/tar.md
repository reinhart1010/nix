---
layout: page
title: common/tar (français)
description: "Utilitaire d'archivage."
content_hash: 6f644b326cfa1be66e5f6d268a65c8a68a5363dd
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/tar.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tar.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tar.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tar.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tar.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tar

Utilitaire d'archivage.
Souvent combiné avec une méthode de compression, telle que gzip ou bzip2.
Plus d'informations : <https://www.gnu.org/software/tar>.

- Crée une archive à partir de fichiers :

`tar cf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/cible.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1 chemin/vers/fichier2 ...</span>

- Crée une archive gzip à partir de fichiers :

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/cible.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1 chemin/vers/fichier2 ...</span>

- Crée une archive gzip à partir d'un répertoire en utilisant son chemin relatif :

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/cible.tar.gz</span>` --directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>` .`

- Extrait une archive (compressée) dans le dossier courant en affichant la liste des fichiers traités :

`tar xvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/source.tar[.gz|.bz2|.xz]</span>

- Extrait une archive (compressée) dans un répertoire cible :

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/source.tar[.gz|.bz2|.xz]</span>` --directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">répertoire</span>

- Crée une archive compressée, en utilisant le suffixe de l'archive pour déterminer le programme de compression :

`tar caf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/cible.tar.xz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1 chemin/vers/fichier2 ...</span>

- Liste les fichiers contenus dans une archive tar :

`tar tvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/source.tar</span>

- Extrait les fichiers correspondant au motif :

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tar</span>` --wildcards "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.html</span>`"`
