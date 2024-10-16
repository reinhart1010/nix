---
layout: page
title: linux/yay (español)
description: "Yet Another Yogurt: crea e instala paquetes desde el repositorio de usuarios de Arch."
content_hash: 9b29eb2015ed3ff4d3c4217c40d17330040ab00b
last_modified_at: 2024-10-16
related_topics:
  - title: Deutsch version
    url: /de/linux/yay.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/yay.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/yay.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/yay.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/yay.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/yay.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yay

Yet Another Yogurt: crea e instala paquetes desde el repositorio de usuarios de Arch.
Vea también `pacman`.
Más información: <https://github.com/Jguer/yay>.

- Busca e instala paquetes de forma interactiva desde los repositorios y AUR:

`yay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_paquete|término_de_búsqueda</span>

- Sincroniza y actualiza todos los paquetes desde los repositorios y AUR:

`yay`

- Sincroniza y actualiza solo paquetes del AUR:

`yay -Sua`

- Instala un nuevo paquete desde los repositorios y AUR:

`yay -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete instalado, sus dependencias y archivos de configuración:

`yay -Rns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Busca en la base de datos de paquetes una palabra clave de los repositorios y AUR:

`yay -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave</span>

- Elimina paquetes huérfanos (instalados como dependencias pero no requeridos por ningún paquete):

`yay -Yc`

- Muestra estadísticas de paquetes instalados y estado del sistema:

`yay -Ps`
