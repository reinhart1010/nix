---
layout: page
title: linux/waypipe (español)
description: "Ejecuta remotamente aplicaciones gráficas bajo un compositor para Wayland."
content_hash: 29b08dda78383aaa56a1277a1ee69173f5656d25
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/linux/waypipe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# waypipe

Ejecuta remotamente aplicaciones gráficas bajo un compositor para Wayland.
Más información: <https://gitlab.freedesktop.org/mstoeckl/waypipe>.

- Ejecuta un programa gráfico remotamente y muestralo localmente:

`waypipe ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Abre un túnel SSH para ejecutar cualquier programa de forma remota y visualizarlo localmente:

`waypipe ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>
