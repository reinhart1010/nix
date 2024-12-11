---
layout: page
title: linux/uname (español)
description: "Uname imprime información sobre la máquina y el sistema operativo que se ejecuta."
content_hash: 88ea76b8f82e041b7d7048a3140f2361b5daa592
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/linux/uname.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/uname.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/uname.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/uname.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/uname.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/uname.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/uname.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/uname.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uname

Uname imprime información sobre la máquina y el sistema operativo que se ejecuta.
Más información: <https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html>.

- Imprime toda la información:

`uname --all`

- Imprime el nombre del kernel:

`uname --kernel-name`

- Imprime el nombre de host de red:

`uname --nodename`

- Imprime la liberación (release) del kernel:

`uname --kernel-release`

- Imprime la versión del kernel:

`uname --kernel-version`

- Imprime el nombre del hardware de la máquina:

`uname --machine`

- Imprime el tipo de procesador:

`uname --processor`

- Imprime el nombre del sistema operativo:

`uname --operating-system`
