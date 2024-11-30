---
layout: page
title: linux/dmenu (español)
description: "Menú dinámico."
content_hash: 45d23185eaba2732203cf03f96b0308eabfba038
last_modified_at: 2024-11-30
related_topics:
  - title: English version
    url: /en/linux/dmenu.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dmenu.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmenu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dmenu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dmenu

Menú dinámico.
Crea un menú a partir de una entrada de texto con cada elemento, en una nueva línea.
Más información: <https://manned.org/dmenu>.

- Muestra un menú a partir de la salida del comando 'ls':

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>` | dmenu`

- Muestra un menú con artículos personalizados separados por una nueva línea (`\n`):

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rojo</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verde</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">azul</span>`" | dmenu`

- Deja que el usuario elija entre varios elementos y guarda el seleccionado en un archivo:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rojo</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verde</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">azul</span>`" | dmenu > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color.txt</span>

- Lanza dmenu en un monitor específico:

`ls | dmenu -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Muestra dmenu en la parte inferior de la pantalla:

`ls | dmenu -b`
