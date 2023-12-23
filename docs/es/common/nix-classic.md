---
layout: page
title: common/nix-classic (español)
description: "Una interfaz clásica y estable para un potente gestor de paquetes que hace la gestión de paquetes fiable, reproducible y declarativa."
content_hash: 9e961b8e38458fab1e42505cbdc12edaf56b9744
last_modified_at: 2023-12-23
related_topics:
  - title: English version
    url: /en/common/nix-classic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nix classic

Una interfaz clásica y estable para un potente gestor de paquetes que hace la gestión de paquetes fiable, reproducible y declarativa.
Algunos comandos Nix como `nix-build`, `nix-shell`, `nix-env`, y `nix-store` tienen sus propias páginas. Ver también: `tldr nix`.
Más información: <https://nixos.org>.

- Busca un paquete en nixpkgs a través de su nombre:

`nix-env -qaP `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">termino_busqueda_regexp</span>

- Inicia un shell con los paquetes especificados disponibles:

`nix-shell -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkg1 pkg2 pkg3...</span>

- Instala algunos paquetes de forma permanente:

`nix-env -iA `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs.pkg1 nixpkgs.pkg2...</span>

- Muestra todas las dependencias de una ruta de almacenamiento (paquete), en formato de árbol:

`nix-store --query --tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>

- Actualiza los canales (repositorios):

`nix-channel --update`

- Elimina rutas no utilizadas del almacén Nix:

`nix-collect-garbage`
