---
layout: page
title: linux/agetty (español)
description: "Alternativa a `getty`: Abre un puerto `tty`, pide un nombre de usuario, e invoca el comando `/bin/login`."
content_hash: 4a962e051d7d2528ec039cc6e51e47c418057589
last_modified_at: 2024-03-27
related_topics:
  - title: English version
    url: /en/linux/agetty.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/agetty.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># agetty

Alternativa a `getty`: Abre un puerto `tty`, pide un nombre de usuario, e invoca el comando `/bin/login`.
Normalmente es invocado por `init`.
Nota: la tasa de baudios es la velocidad de transferencia de datos entre una terminal y un dispositivo a través de una conexión serie.
Más información: <https://manned.org/agetty>.

- Conecta `stdin` a un puerto (relativo a `/dev`) y especifica opcionalmente una tasa de baudios (por predeterminado 9600):

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>

- Asume que `stdin` ya está conectado a una `tty` y establece un [t]iempo de espera para el inicio de sesión:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--timeout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tiempo_de_espera_en_segundos</span>` -`

- Asume que `tty` es de [8]-bits, anulando la variable de entorno `TERM` establecida por `init`:

`agetty -8 - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">term_var</span>

- Omite el inicio de sesión ([n]o inicio de sesión) e invoca, como superusuario, otro programa de inicio de sesión en lugar de `/bin/login`:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--skip-login</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--login-program</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">login_program</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty</span>

- No muestra el archivo de pre-inicio de sesión ([i]ssue) (`/etc/issue` por predeterminado) antes de escribir el mensaje de inicio de sesión:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--noissue</span>` -`

- Cambia el directorio [r]aíz y escribe un falso [H]ost específico en el archivo `utmp`:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/raíz_directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-H|--host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fake_host</span>` -`
