---
layout: page
title: common/afconvert (français)
description: "Convertir entre les formats de fichiers AFF et brut."
content_hash: 37ccaede6863b5a6a18e26480964872e90a632e4
last_modified_at: 2023-11-22
related_topics:
  - title: English version
    url: /en/common/afconvert.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/afconvert.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/afconvert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/afconvert.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/afconvert.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/afconvert.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># afconvert

Convertir entre les formats de fichiers AFF et brut.
Plus d'informations : <https://manned.org/afconvert.1>.

- Utiliser une extension spécifique (par défaut: `aff`) :

`afconvert -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_de_sortie1 chemin/vers/fichier_de_sortie2 ...</span>

- Utiliser un niveau de compression spécifique (par défaut: `7`) :

`afconvert -X`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_de_sortie1 chemin/vers/fichier_de_sortie2 ...</span>
