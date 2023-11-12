---
layout: page
title: osx/textutil (español)
description: "Manipula archivos de texto en varios formatos."
content_hash: 7681b1882af0c66981d59aeed84d8eb9ad2e48b9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/textutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/textutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# textutil

Manipula archivos de texto en varios formatos.
Más información: <https://ss64.com/osx/textutil.html>.

- Muestra información de `foo.rtf`:

`textutil -info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.rtf</span>

- Convierte `foo.rtf` en `foo.html`:

`textutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.rtf</span>

- Convierte texto enriquecido a texto normal:

`textutil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.rtf</span>` -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>

- Convierte `foo.txt` en `foo.rtf`, usando la fuente Times con un tamaño 10:

`textutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtf</span>` -font `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Times</span>` -fontsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.txt</span>

- Carga todos los archivos RTF en el directorio actual, concatena su contenido y escribe el resultado como `index.html` con el título HTML establecido en "Varios archivos":

`textutil -cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` -title "Varios archivos" -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` *.rtf`
