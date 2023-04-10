---
layout: page
title: common/ansible-inventory (español)
description: "Muestra o vuelca un inventario de Ansible."
content_hash: 8104a3d81d2dc97933ddc39a855b2c914e727103
last_modified_at: 2023-04-10
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-inventory.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-inventory.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-inventory.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ansible-inventory

Muestra o vuelca un inventario de Ansible.
Ver también: `ansible`.
Más información: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Muestra el inventario por defecto:

`ansible-inventory --list`

- Muestra un inventario personalizado:

`ansible-inventory --list --inventory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_script_o_directorio</span>

- Muestra el inventario por defecto en YAML:

`ansible-inventory --list --yaml`

- Vuelca el inventario por defecto a un fichero:

`ansible-inventory --list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
