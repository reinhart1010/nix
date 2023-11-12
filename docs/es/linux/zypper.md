---
layout: page
title: linux/zypper (español)
description: "Utilidad para la gestión de paquetes en SUSE y openSUSE."
content_hash: e7b81cd9d9f6d92b7357b5971e089a9e971201eb
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/zypper.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/zypper.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/zypper.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/zypper.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/zypper.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zypper.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/zypper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zypper

Utilidad para la gestión de paquetes en SUSE y openSUSE.
Más información: <https://en.opensuse.org/SDB:Zypper_manual>.

- Sincroniza la lista de paquetes y versiones disponibles:

`zypper refresh`

- Instala un nuevo paquete:

`zypper install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete:

`zypper remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Actualiza los paquetes instalados a la versión más reciente disponible:

`zypper update`

- Busca en los repositorios un paquete mediante una palabra clave:

`zypper search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave</span>

- Muestra información relacionada con los repositorios configurados:

`zypper repos --sort-by-priority`
