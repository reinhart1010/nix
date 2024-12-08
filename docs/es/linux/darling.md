---
layout: page
title: linux/darling (español)
description: "Ejecuta software macOS en Linux."
content_hash: b687edb3e3e0e7f615cc00931e30fe385fdfa420
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/darling.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/darling.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># darling

Ejecuta software macOS en Linux.
Más información: <https://darlinghq.org>.

- Ejecuta un comando integrado:

`darling shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uname</span>

- Ejecuta un programa específico en el directorio actual con argumentos:

`darling shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./program</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa_argumento_1 programa_argumento_2 ...</span>

- Abre una interfaz de comandos de macOS:

`darling shell`

- Apaga el servicio:

`darling shutdown`
