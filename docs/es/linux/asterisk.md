---
layout: page
title: linux/asterisk (español)
description: "Ejecuta y administra instancias de servidores telefónicos e intercambiadores (teléfonos)."
content_hash: 2f512eafe9a81409f80eb699b4a1f8c90bcd764c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/asterisk.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/asterisk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/asterisk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asterisk

Ejecuta y administra instancias de servidores telefónicos e intercambiadores (teléfonos).
Más información: <https://docs.asterisk.org>.

- [R]econecta a un servidor en ejecución y activa el registro con 3 niveles de [v]erbosidad:

`asterisk -r -vvv`

- [R]econecta a un servidor en ejecución, ejecuta un solo comando y regresa:

`asterisk -r -x "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Muestra los clientes chan_SIP (teléfonos):

`asterisk -r -x "sip show peers"`

- Muestra las llamadas y canales activos:

`asterisk -r -x "core show channels"`

- Muestra los buzones de voz:

`asterisk -r -x "voicemail show users"`

- Termina un canal:

`asterisk -r -x "hangup request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID_del_canal</span>`"`

- Recarga la configuración de chan_SIP:

`asterisk -r -x "sip reload"`
