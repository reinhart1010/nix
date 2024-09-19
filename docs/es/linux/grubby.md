---
layout: page
title: linux/grubby (español)
description: "Herramienta para configurar los gestores de arranque `grub` y `zipl`."
content_hash: 0192d27145acfc96e74ebfba6bfea62582237e0d
last_modified_at: 2024-09-19
related_topics:
  - title: English version
    url: /en/linux/grubby.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grubby

Herramienta para configurar los gestores de arranque `grub` y `zipl`.
Más información: <https://manned.org/grubby.8>.

- Añade argumentos de arranque del núcleo a todas las entradas del menú del núcleo:

`sudo grubby --update-kernel=ALL --args '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet console=ttyS0</span>`'`

- Elimina los argumentos existentes de la entrada para el núcleo por defecto:

`sudo grubby --update-kernel=DEFAULT --remove-args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet</span>

- Lista todas las entradas del menú del núcleo:

`sudo grubby --info=ALL`
