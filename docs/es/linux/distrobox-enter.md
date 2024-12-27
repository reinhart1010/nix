---
layout: page
title: linux/distrobox-enter (español)
description: "Entra a un contenedor Distrobox. Véase también: `tldr distrobox`."
content_hash: 5f07267f897b0c14e4bdfccd07cf488b853f9422
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/distrobox-enter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-enter

Entra a un contenedor Distrobox. Véase también: `tldr distrobox`.
El comando ejecutado por defecto es su SHELL, pero puede especificar otros o comandos enteros a ejecutar. Si se utiliza dentro de un script, una aplicación o un servicio, puede utilizar el modo `--headless` para desactivar tty e interactividad.
Más información: <https://distrobox.it/usage/distrobox-enter>.

- Entra a un contenedor Distrobox:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Entra a un contenedor Distrobox y ejecuta un comando al iniciar sesión:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh -l</span>

- Entra a un contenedor Distrobox sin instanciar una tty:

`distrobox-enter --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uptime -p</span>
