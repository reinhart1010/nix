---
layout: page
title: osx/emond (español)
description: "Servicio de Monitor de Eventos que acepta eventos de varios servicios, los ejecuta a través de un simple motor de reglas, y toma acciones."
content_hash: e459290f63b728433cd66991c3c362868bc208b7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/emond.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/emond.html
    icon: bi bi-globe
tldri18n_status: 2
---
# emond

Servicio de Monitor de Eventos que acepta eventos de varios servicios, los ejecuta a través de un simple motor de reglas, y toma acciones.
Las acciones pueden ejecutar comandos, enviar correos electrónicos o mensajes SMS.
Más información: <https://www.manpagez.com/man/8/emond/>.

- Inicia el daemon:

`emond`

- Especifica las reglas que emond debe procesar indicando una ruta a un archivo o directorio:

`emond -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Utiliza un archivo de configuración específico:

`emond -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_configuración</span>
