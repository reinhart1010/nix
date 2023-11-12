---
layout: page
title: osx/open (español)
description: "Abre archivos, directorios y aplicaciones."
content_hash: 9bfac2ebbf8464c092def56371e65ccd4d6672cb
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/osx/open.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/open.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/open.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/open.html
    icon: bi bi-globe
tldri18n_status: 2
---
# open

Abre archivos, directorios y aplicaciones.
Más información: <https://ss64.com/osx/open.html>.

- Abre un archivo con la aplicación asociada:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.ext</span>

- Ejecuta una [a]plicación gráfica de macOS:

`open -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplicacion</span>`"`

- Ejecuta una aplicación gráfica de macOS basada en el identificador [b]undle (consulta `osascript` para obtenerlo fácilmente):

`open -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domain.application</span>

- Abre el directorio actual en Finder:

`open .`

- Abre un archivo en Finder:

`open -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre todos los archivos de una extensión determinada en el directorio actual con la aplicación asociada:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>

- Abre una [n]ueva instancia de una aplicación especificada mediante un identificador [b]undle:

`open -n -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domain.application</span>
