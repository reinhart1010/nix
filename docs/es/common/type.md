---
layout: page
title: common/type (español)
description: "Muestra el tipo de comando que ejecutará el intérprete de comandos."
content_hash: 859d5774a447511e6330c3ce583c8140302b08df
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/common/type.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/type.html
    icon: bi bi-globe
tldri18n_status: 2
---
# type

Muestra el tipo de comando que ejecutará el intérprete de comandos.
Nota: todos los ejemplos no son compatibles con POSIX.
Más información: <https://manned.org/type>.

- Muestra el tipo de un comando:

`type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Muestra todas las rutas con el ejecutable especificado (solo funciona en los intérpretes de comandos Bash/fish/Zsh):

`type -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Muestra el nombre del archivo en disco que se ejecutaría (solo funciona en intérpretes de comandos Bash/fish/Zsh):

`type -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Muestra el tipo de un comando específico, alias/palabra clave/función/integrado/archivo (solo funciona en intérpretes de comandos Bash/fish):

`type -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
