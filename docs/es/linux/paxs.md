---
layout: page
title: linux/paxs (español)
description: "Gestiona paquetes a través de Yay, Flatpak y Snap."
content_hash: f778a64216b19e92fcdc0ceed20e2e1ea365e19e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/paxs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paxs

Gestiona paquetes a través de Yay, Flatpak y Snap.
Admite la búsqueda, instalación, eliminación y actualización de paquetes.
Más información: <https://github.com/zamhedonia/paxs>.

- Busca un paquete:

`paxs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">término_de_búsqueda</span>

- Actualiza todos los paquetes:

`paxs -u`

- Instala un paquete (solicitando el código fuente):

`paxs -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete (solicitando la fuente):

`paxs -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Busca actualizaciones en todos los gestores de paquetes:

`paxs -c`

- Muestra la ayuda:

`paxs -h`
