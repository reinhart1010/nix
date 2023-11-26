---
layout: page
title: osx/plutil (español)
description: "Ve, convierte, valida o edita archivos de listas de propiedades (\"plist\")."
content_hash: bf5ea102de2a506aa5c44fb428ca39537ef92932
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/osx/plutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# plutil

Ve, convierte, valida o edita archivos de listas de propiedades ("plist").
Más información: <https://www.manpagez.com/man/1/plutil/>.

- Muestra el contenido de uno o más archivos plist en un formato legible por humanos:

`plutil -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo1.plist archivo2.plist ...</span>

- Convierte uno o varios archivos plist a formato XML, sobrescribiendo los archivos originales:

`plutil -convert xml1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo1.plist archivo2.plist ...</span>

- Convierte uno o más archivos plist a formato binario, sobrescribiendo los archivos originales en su lugar:

`plutil -convert binary1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo1.plist archivo2.plist ...</span>

- Convierte un archivo plist a un formato diferente, escribiendo en un nuevo archivo:

`plutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml1|binary1|json|swift|objc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.plist</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/nuevo_archivo.plist</span>

- Convierte un archivo plist a un formato diferente, escribiendo en `stdout`:

`plutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml1|binary1|json|swift|objc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.plist</span>` -o -`
