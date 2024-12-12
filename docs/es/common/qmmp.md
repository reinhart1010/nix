---
layout: page
title: common/qmmp (español)
description: "Un reproductor de audio con una interfaz similar a Winamp o XMMS."
content_hash: 2ab960968339a9b57b06f8069d0132b575c87c69
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/common/qmmp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qmmp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/qmmp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qmmp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qmmp

Un reproductor de audio con una interfaz similar a Winamp o XMMS.
Vea también: `clementine`, `ncmpcpp`, `cmus`.
Más información: <https://qmmp.ylsoftware.com>.

- Lanza la interfaz gráfica de usuario (GUI):

`qmmp`

- Comienza o detiene el audio actual:

`qmmp --play-pause`

- Va hacia adelante o hacia atrás una cantidad específica de tiempo en segundos:

`qmmp --seek-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fwd|bwd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tiempo_en_segundos</span>

- Reproduce el próximo archivo de audio:

`qmmp --next`

- Reproduce el archivo de audio anterior:

`qmmp --previous`

- Muestra el volumen actual:

`qmmp --volume-status`

- [inc]rementa o [dec]rementa el volumen del audio actual en un 5%:

`qmmp --volume-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc|dec</span>
