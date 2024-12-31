---
layout: page
title: common/suspend (español)
description: "Suspende la ejecución del intérprete de comandos actual."
content_hash: 60db90f1aad0a88634e97247fee58ab05ba2cacf
last_modified_at: 2024-12-31
related_topics:
  - title: English version
    url: /en/common/suspend.html
    icon: bi bi-globe
tldri18n_status: 2
---
# suspend

Suspende la ejecución del intérprete de comandos actual.
Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-suspend>.

- Suspende el intérprete de comandos actual (útil para cuando está con intérpretes de comandos anidados como `su`):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>` <Intro> suspend`

- Ejecuta en un terminal separado para continuar desde la suspensión si `suspend` fue usado en un intérprete de comandos no anidado:

`pkill -CONT bash`

- Fuerza la suspensión, incluso si esto bloquea el sistema:

`suspend -f`
