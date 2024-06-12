---
layout: page
title: linux/agetty (español)
description: "Alternativa a `getty`: Abre un puerto `tty`, pide un nombre de usuario, e invoca el comando `/bin/login`."
content_hash: 282d55ae6d77078f4d069c0f931622c6ffbfd969
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/linux/agetty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# agetty

Alternativa a `getty`: Abre un puerto `tty`, pide un nombre de usuario, e invoca el comando `/bin/login`.
Normalmente es invocado por `init`.
Nota: la tasa de baudios es la velocidad de transferencia de datos entre una terminal y un dispositivo a través de una conexión serie.
Más información: <https://manned.org/agetty>.

- Conecta `stdin` a un puerto (relativo a `/dev`) y especifica opcionalmente una tasa de baudios (cuyo valor predeterminado es 9600):

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>

- Asume que `stdin` ya está conectado a una `tty` y establece un tiempo de espera para el inicio de sesión:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--timeout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tiempo_de_espera_en_segundos</span>` -`

- Asume que `tty` es de [8]-bits, sobreescribiendo la variable de entorno `TERM` establecida por `init`:

`agetty -8 - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_term</span>

- Omite el inicio de sesión e invoca, como superusuario, otro programa de inicio de sesión en lugar de `/bin/login`:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--skip-login</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--login-program</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa_de_inicio_de_sesión</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty</span>

- Escribe el mensaje de inicio de sesión sin mostrar el contenido del archivo de pre-inicio de sesión (`/etc/issue` por predeterminado):

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--noissue</span>` -`

- Cambia el directorio raíz y escribe un host falso en el archivo `utmp`:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/raíz_directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-H|--host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_falso</span>` -`
