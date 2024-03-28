---
layout: page
title: linux/waypipe (español)
description: "Ejecuta remotamente aplicaciones gráficas bajo un compositor para Wayland."
content_hash: cb1e2903629f0b1414406cabca56cc32f469722d
last_modified_at: 2024-03-28
related_topics:
  - title: English version
    url: /en/linux/waypipe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# waypipe

Ejecuta remotamente aplicaciones gráficas bajo un compositor para Wayland.
Más información: <https://gitlab.freedesktop.org/mstoeckl/waypipe>.

- Ejecuta un programa gráfico remotamente y lo muestra localmente:

`waypipe ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Abre un túnel SSH para ejecutar cualquier programa de forma remota y lo visualiza localmente:

`waypipe ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@{servidor</span>
