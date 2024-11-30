---
layout: page
title: linux/wine (español)
description: "Ejecuta programas de Windows en sistemas basados en Unix."
content_hash: c2bbdc4dc9e980ae3102540cc76f0b214e843c82
last_modified_at: 2024-11-30
related_topics:
  - title: English version
    url: /en/linux/wine.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/wine.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/wine.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/wine.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wine

Ejecuta programas de Windows en sistemas basados en Unix.
Más información: <https://wiki.winehq.org/>.

- Ejecuta un programa específico dentro del ambiente `wine`:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Ejecuta un programa específico en segundo plano (background):

`wine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Instala/desinstala un paquete MSI:

`wine msiexec /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i|x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/package.msi</span>

- Ejecuta `File Explorer`, `Notepad`, o `WordPad`:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">explorer|notepad|write</span>

- Ejecuta `Registry Editor`, `Control Panel` o `Task Manager`:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regedit|control|taskmgr</span>

- Ejecuta la herramienta de configuración:

`wine winecfg`
