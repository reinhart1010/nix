---
layout: page
title: linux/dnf-config-manager (español)
description: "Administra opciones de configuración y repositorios DNF en sistemas basados en Fedora."
content_hash: e9f33ecf1f29bcb88014a8393d9cfebab6a06135
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dnf-config-manager.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dnf-config-manager.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dnf-config-manager.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dnf-config-manager.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnf config-manager

Administra opciones de configuración y repositorios DNF en sistemas basados en Fedora.
Más información: <https://manned.org/dnf-config-manager>.

- Agrega (y activa) un repositorio de una URL:

`dnf config-manager --add-repo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_del_repositorio</span>

- Imprime los valores de configuración actuales:

`dnf config-manager --dump`

- Habilita un repositorio específico:

`dnf config-manager --set-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_del_repositorio</span>

- Deshabilita repositorios especificados:

`dnf config-manager --set-disabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_del_repositorio1 identificador_del_repositorio2 ...</span>

- Establece una opción de configuración para un repositorio:

`dnf config-manager --setopt=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opción</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Muestra la ayuda:

`dnf config-manager --help-cmd`
