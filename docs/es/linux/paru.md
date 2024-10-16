---
layout: page
title: linux/paru (español)
description: "Un asistente del AUR y envoltorio para pacman."
content_hash: 0e7e50905cc3378ea74d5aa27f76a34a23af7b89
last_modified_at: 2024-10-16
related_topics:
  - title: Deutsch version
    url: /de/linux/paru.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/paru.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/paru.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/paru.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/paru.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># paru

Un asistente del AUR y envoltorio para pacman.
Más información: <https://github.com/Morganamilo/paru>.

- Busca e instala un paquete de forma interactiva:

`paru `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_paquete_o_término_de_búsqueda</span>

- Sincroniza y actualiza todos los paquetes:

`paru`

- Actualiza paquetes del AUR:

`paru -Sua`

- Obtiene información acerca del paquete:

`paru -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Descarga `PKGBUILD` y otros archivos fuente del paquete desde AUR o ABS:

`paru --getpkgbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Muestra el archivo `PKGBUILD` de un paquete:

`paru --getpkgbuild --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>
