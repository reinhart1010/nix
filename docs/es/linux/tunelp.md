---
layout: page
title: linux/tunelp (español)
description: "Establece varios parámetros para dispositivos de puerto paralelo para la solución de problemas o para un mejor rendimiento."
content_hash: 5a0661850198f1e7a96bf3c11fd65dbc103eb6bd
last_modified_at: 2024-04-04
related_topics:
  - title: English version
    url: /en/linux/tunelp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tunelp

Establece varios parámetros para dispositivos de puerto paralelo para la solución de problemas o para un mejor rendimiento.
Parte de `util-linux`.
Más información: <https://manned.org/tunelp>.

- Comprueba el e[s]tado de un dispositivo de puerto paralelo:

`tunelp --status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/lp0</span>

- Restablece un puerto paralelo:

`tunelp --reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/lp0</span>

- Utiliza un [i]RQ dado para un dispositivo, cada uno representando una línea de interrupción:

`tunelp -i 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/lp0</span>

- Intenta imprimir varias veces un [c]arácter en la impresora antes de permanecer inactiva durante un [t]iempo determinado:

`tunelp --chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">veces</span>` --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tiempo_en_centisegundos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/lp0</span>

- Activa o desactiva el [a]bortar por error (desactivado por defecto):

`tunelp --abort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>
