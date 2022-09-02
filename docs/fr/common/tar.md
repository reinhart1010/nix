---
layout: page
title: common/tar (français)
description: "Utilitaire d'archivage."
content_hash: 5c6c5e06dba224129d8f260d547b04ca7f64ba19
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
  - title: 中文 version
    url: /zh/common/tar.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tar

Utilitaire d'archivage.
Souvent combiné avec une méthode de compression, telle que gzip ou bzip2.
Plus d'informations : <https://www.gnu.org/software/tar>.

- Crée une archive à partir de fichiers :

`tar cf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cible.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier1 fichier2 fichier3</span>

- Crée une archive gzip :

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cible.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier1 fichier2 fichier3</span>

- Extrait une archive (compressée) dans le dossier courant :

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tar[.gz|.bz2|.xz]</span>

- Extrait une archive dans un dossier cible :

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tar</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dossier</span>

- Crée une archive compressée, en utilisant le suffixe de l'archive pour déterminer le programme de compression :

`tar caf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cible.tar.xz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier1 fichier2 fichier3</span>

- Liste le contenu d'une archive tar :

`tar tvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tar</span>

- Extrait les fichiers correspondant au motif :

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.tar</span>` --wildcards "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.html</span>`"`
