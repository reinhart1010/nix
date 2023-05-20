---
layout: page
title: osx/xsltproc (español)
description: "Transforma XML con XSLT para producir una salida (normalmente HTML o XML)."
content_hash: 091639d10417b4ec8db1d9e4c35b1a2ea5a6a047
last_modified_at: 2023-05-20
related_topics:
  - title: English version
    url: /en/osx/xsltproc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/xsltproc.html
    icon: bi bi-globe
---
# xsltproc

Transforma XML con XSLT para producir una salida (normalmente HTML o XML).
Más información: <http://www.xmlsoft.org/xslt/xsltproc.html>.

- Transforma un archivo XML con una hoja de estilos XSLT específica:

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_salida.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_hoja_estilo.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.xml</span>

- Pasa un valor a un parámetro de la hoja de estilos:

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_salida.html</span>` --stringparam "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_hoja_estilo.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_xml.xml</span>
