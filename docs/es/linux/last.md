---
layout: page
title: linux/last (español)
description: "Lista la información de los últimos inicios de sesión de usuario."
content_hash: de8f040adc2e3b2967ac9ff689563dd9c0646a68
last_modified_at: 2024-04-12
related_topics:
  - title: English version
    url: /en/linux/last.html
    icon: bi bi-globe
tldri18n_status: 2
---
# last

Lista la información de los últimos inicios de sesión de usuario.
Vea también: `lastb`, `login`.
Más información: <https://manned.org/last.1>.

- Lista la información de inicio de sesión (por ejemplo, nombre de usuario, terminal, tiempo de arranque, núcleo) de todos los usuarios:

`last`

- Lista la información de inicio de sesión de un usuario específico:

`last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>

- Muestra la información de una terminal específica:

`last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty1</span>

- Lista la información actualizada (por defecto, la más reciente aparece al principio):

`last | tac`

- Muestra información sobre el arranque del sistema:

`last "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system boot</span>`"`

- Lista información con un formato de [t]iempo específico:

`last --time-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notime|full|iso</span>

- Lista información desde una fecha y hora específica:

`last --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-7days</span>

- Muestra información (es decir, nombre e IP) de hosts remotos:

`last --dns`
