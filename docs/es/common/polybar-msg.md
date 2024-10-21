---
layout: page
title: common/polybar-msg (español)
description: "Controla `polybar` utilizando mensajería entre procesos (IPC)."
content_hash: 2402e1d034cc4477db1e244b0daaba9eb117ab23
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/polybar-msg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# polybar-msg

Controla `polybar` utilizando mensajería entre procesos (IPC).
Nota: IPC está desactivado por defecto y se puede habilitar configurando `enable-ipc = true` en la configuación de Polybar.
Más información: <https://polybar.rtfd.io/en/stable/user/ipc.html>.

- Cierra la barra:

`polybar-msg cmd quit`

- Reinicia la barra en su lugar:

`polybar-msg cmd restart`

- Oculta la barra (no hace nada si la barra ya está oculta):

`polybar-msg cmd hide`

- Muestra la barra nuevamente (no hace nada si la barra no está oculta):

`polybar-msg cmd show`

- Alterna entre oculto/visible:

`polybar-msg cmd toggle`

- Ejecuta una acción de módulo (la cadena de datos es opcional):

`polybar-msg action "#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_módulo</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_acción</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_de_datos</span>`"`

- Envía mensajes solo a una instancia específica de Polybar (todas las instancias por defecto):

`polybar-msg -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmd|action</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">carga</span>
