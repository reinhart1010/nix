---
layout: page
title: common/simplehttpserver (español)
description: "Un simple servidor HTTP/S que soporta subida de ficheros, autenticación básica y reglas YAML para respuestas personalizadas."
content_hash: 061b30c64ac491670f9f5a7ee545f633a0014e1e
last_modified_at: 2024-03-17
related_topics:
  - title: English version
    url: /en/common/simplehttpserver.html
    icon: bi bi-globe
tldri18n_status: 2
---
# simplehttpserver

Un simple servidor HTTP/S que soporta subida de ficheros, autenticación básica y reglas YAML para respuestas personalizadas.
Una alternativa Go a `http.server` de Python.
Más información: <https://github.com/projectdiscovery/simplehttpserver>.

- Inicia el servidor HTTP que sirve el directorio actual con salida verbosa (escucha en todas las interfaces y puerto 8000 por defecto):

`simplehttpserver -verbose`

- Inicia el servidor HTTP con autenticación básica sirviendo una ruta específica a través del puerto 80 en todas las interfaces:

`sudo simplehttpserver -basic-auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` -path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/www/html</span>` -listen 0.0.0.0:80`

- Inicia el servidor HTTP, habilitando HTTPS utilizando un certificado autofirmado con SAN personalizado en todas las interfaces:

`sudo simplehttpserver -https -domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.selfsigned.com</span>` -listen 0.0.0.0:443`

- Inicia el servidor HTTP con cabeceras de respuesta personalizadas y capacidad de carga:

`simplehttpserver -upload -header '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X-Powered-By: Go</span>`' -header '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Server: SimpleHTTPServer</span>`'`

- Inicia el servidor HTTP con reglas personalizables en YAML (consulte la documentación para DSL):

`simplehttpserver -rules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rules.yaml</span>
