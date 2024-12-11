---
layout: page
title: linux/qm-guest-exec (español)
description: "Ejecuta una orden específica a través de un agente huésped."
content_hash: 61523e9ebaac3cd7f0e03ef07b222494f7e5ee69
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/linux/qm-guest-exec.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/qm-guest-exec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-guest-exec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm guest exec

Ejecuta una orden específica a través de un agente huésped.
Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Ejecuta una orden específica a través de un agente huésped:

`qm guest exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primer_argumento segundo_argumento ...</span>

- Ejecuta una orden específica a través de un agente huésped asincrónicamente:

`qm guest exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primer_argumento segundo_argumento ...</span>` --synchronous 0`

- Ejecuta una orden específica a través de un agente huésped con un tiempo máximo de 10 segundos:

`qm guest exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primer_argumento segundo_argumento...</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Ejecuta una orden específica a través de un agente huésped y reenvía la entrada de `stdin` hasta el fin del archivo (EOF) al agente huésped:

`qm guest exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primer_argumento segundo_argumento ...</span>` --pass-stdin 1`
