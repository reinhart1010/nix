---
layout: page
title: linux/xcowsay (español)
description: "Muestra una linda vaca y un mensaje en el escritorio de Linux."
content_hash: 622573b46693a20de26edd4722743ee27f64eb72
last_modified_at: 2024-12-01
related_topics:
  - title: English version
    url: /en/linux/xcowsay.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/xcowsay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/xcowsay.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xcowsay.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xcowsay

Muestra una linda vaca y un mensaje en el escritorio de Linux.
La vaca se muestra por una cantidad fija de tiempo, o una cantidad de tiempo calculado a partir del tamaño del texto. Haga clic en la vaca para despedirla inmediatamente.
Más información: <https://www.doof.me.uk/xcowsay/>.

- Muestra una vaca diciendo "hola, mundo":

`xcowsay "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hola, mundo</span>`"`

- Muestra una vaca con salida desde otro comando:

`ls | xcowsay`

- Muestra una vaca en las coordenadas X e Y especificadas:

`xcowsay --at=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Y</span>

- Muestra una vaca de tamaño diferente:

`xcowsay --cow-size=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">small|med|large</span>

- Muestra una burbuja de pensamiento en lugar de una burbuja de discurso:

`xcowsay --think`

- Muestra una imagen diferente en lugar de la vaca predeterminada:

`xcowsay --image=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
