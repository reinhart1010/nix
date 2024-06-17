---
layout: page
title: linux/pw-metadata (español)
description: "Supervisa, establece y elimina metadatos en objetos PipeWire."
content_hash: 3d96d95d9b3fb1be02d35c07a36ec3474adf3417
last_modified_at: 2024-06-17
related_topics:
  - title: English version
    url: /en/linux/pw-metadata.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-metadata

Supervisa, establece y elimina metadatos en objetos PipeWire.
Vea también: `pipewire`, `pw-mon`, `pw-cli`.
Más información: <https://docs.pipewire.org/page_man_pw-metadata_1.html>.

- Muestra metadatos en el formato por defecto:

`pw-metadata`

- Muestra metadatos con el identificador 0 en `settings`:

`pw-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">settings</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>

- Lista todos los objetos de metadatos disponibles:

`pw-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>

- Continua ejecutando y registrando los cambios en los metadatos:

`pw-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--monitor</span>

- Elimina todos los metadatos:

`pw-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>

- Ajusta `log.level` a 1 en `settings`:

`pw-metadata --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">settings</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">log.level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Muestra ayuda:

`pw-metadata --help`
