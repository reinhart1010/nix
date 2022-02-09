---
layout: page
title: linux/xfreerdp (català)
description: "Implementació lliure del protocol d'escriptori remot (_Remote Desktop Protocol_)."
content_hash: 968eded64c7b0663cb1354d2de0f688a1ca3bfc7
related_topics:
  - title: English version
    url: /en/linux/xfreerdp.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/xfreerdp.html
    icon: bi bi-globe
---
# xfreerdp

Implementació lliure del protocol d'escriptori remot (_Remote Desktop Protocol_).
Més informació: <https://www.freerdp.com>.

- Connecta amb un servidor FreeRDP:

`xfreerdp /u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>` /p:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contrasenya</span>` /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direcció_ip</span>

- Connecta amb un servidor FreeRDP i activa la redirecció d'audio fent servir un dispositiu `sys:alsa`:

`xfreerdp /u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>` /p:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contrassenya</span>` /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">direcció_ip</span>` /sound:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sys:alsa</span>
