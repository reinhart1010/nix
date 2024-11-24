---
layout: page
title: common/pamenlarge (español)
description: "Agranda una imagen PAM duplicando píxeles."
content_hash: af5e91d111524dbe81bda347770cd61349b9db58
last_modified_at: 2024-11-24
related_topics:
  - title: English version
    url: /en/common/pamenlarge.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pamenlarge.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamenlarge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamenlarge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamenlarge

Agranda una imagen PAM duplicando píxeles.
Vea también: `pbmreduce`, `pamditherbw`, `pbmpscale`.
Más información: <https://netpbm.sourceforge.net/doc/pamenlarge.html>.

- Amplía la imagen especificada por el factor dado:

`pamenlarge -scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pam</span>

- Amplía la imagen especificada por los factores especificados horizontal y verticalmente:

`pamenlarge -xscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XN</span>` -yscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pam</span>
