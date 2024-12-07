---
layout: page
title: common/adb-reboot (español)
description: "Reinicia un dispositivo Android o un emulador conectado."
content_hash: 3ba2a9bb140b79e01f62efd0d973f05112d54066
last_modified_at: 2024-12-07
related_topics:
  - title: English version
    url: /en/common/adb-reboot.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-reboot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adb-reboot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-reboot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/adb-reboot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># adb reboot

Reinicia un dispositivo Android o un emulador conectado.
Más información: <https://manned.org/adb>.

- Reinicia el dispositivo normalmente:

`adb reboot`

- Reinicia el dispositivo en modo bootloader:

`adb reboot bootloader`

- Reinicia el dispositivo en modo de recuperación:

`adb reboot recovery`

- Reinicia el dispositivo en modo de arranque rápido:

`adb reboot fastboot`
