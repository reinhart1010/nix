---
layout: page
title: common/olevba (español)
description: "Analiza archivos OLE y OpenXML (p. ej., DOC, XLS, PPT, etc.) para extraer macros VBA, desofuscar y analizar código malicioso."
content_hash: a3071c73457ff46b3d5a27e3988bb163fde99797
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/olevba.html
    icon: bi bi-globe
tldri18n_status: 2
---
# olevba

Analiza archivos OLE y OpenXML (p. ej., DOC, XLS, PPT, etc.) para extraer macros VBA, desofuscar y analizar código malicioso.
Parte de la suite `python-oletools`.
Más información: <https://github.com/decalage2/oletools>.

- Analiza un archivo, mostrando tanto el código de la macro como los resultados del análisis:

`olevba `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Analiza recursivamente todos los archivos compatibles de un directorio:

`olevba -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Proporciona una contraseña para los archivos cifrados de Microsoft Office (puede repetirse):

`olevba --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_encriptado</span>

- Muestra solo los resultados del análisis, sin mostrar el código fuente de la macro:

`olevba -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra solo el código fuente de la macro:

`olevba -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra cadenas ofuscadas y su contenido decodificado:

`olevba --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
