---
layout: page
title: linux/waypipe (español)
description: "Ejecuta remotamente aplicaciones gráficas bajo un compositor para Wayland."
content_hash: 29b08dda78383aaa56a1277a1ee69173f5656d25
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/waypipe.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/waypipe.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># waypipe

Ejecuta remotamente aplicaciones gráficas bajo un compositor para Wayland.
Más información: <https://gitlab.freedesktop.org/mstoeckl/waypipe>.

- Ejecuta un programa gráfico remotamente y muestralo localmente:

`waypipe ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Abre un túnel SSH para ejecutar cualquier programa de forma remota y visualizarlo localmente:

`waypipe ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>
