---
layout: page
title: common/zsh (español)
description: "Z SHell, un intérprete de línea de comandos compatible con Bash."
content_hash: df495302a4056f814bf452a7094b8ac5b3f48458
last_modified_at: 2024-05-03
related_topics:
  - title: Deutsch version
    url: /de/common/zsh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/zsh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/zsh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zsh.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zsh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zsh

Z SHell, un intérprete de línea de comandos compatible con Bash.
Vea también `histexpand` para la expansión del historial.
Más información: <https://www.zsh.org>.

- Comienza una sesión interactiva en el intérprete de comandos:

`zsh`

- Ejecuta un comando y sale:

`zsh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Ejecuta un script:

`zsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.zsh</span>

- Comprueba si hay errores de sintaxis en un script sin ejecutarlo:

`zsh --no-exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.zsh</span>

- Ejecuta comandos desde `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | zsh`

- Ejecuta un script, mostrando cada comando antes de ejecutarlo:

`zsh --xtrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.zsh</span>

- Comienza una sesión interactiva en el intérprete de comandos en modo detallado, mostrando cada comando antes de ejecutarlo:

`zsh --verbose`

- Ejecuta un comando dentro de `zsh` con patrones glob desactivados:

`noglob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
