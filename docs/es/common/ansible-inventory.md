---
layout: page
title: common/ansible-inventory (español)
description: "Muestra o vuelca un inventario de Ansible."
content_hash: a05ad4b59a5290eee47871ec8f8492a0a738c2cd
last_modified_at: 2024-01-07
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
tldri18n_status: 2
---
# ansible-inventory

Muestra o vuelca un inventario de Ansible.
Vea también: `ansible`.
Más información: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Muestra el inventario por defecto:

`ansible-inventory --list`

- Muestra un inventario personalizado:

`ansible-inventory --list --inventory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_script_o_directorio</span>

- Muestra el inventario por defecto en YAML:

`ansible-inventory --list --yaml`

- Vuelca el inventario por defecto a un fichero:

`ansible-inventory --list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
