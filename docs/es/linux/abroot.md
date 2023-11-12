---
layout: page
title: linux/abroot (español)
description: "La utilidad ABRoot proporciona inmutabilidad y atomicidad completas al realizar transacciones entre 2 estados de partición raíz (A⟺B)."
content_hash: 296cb45bcd1da7b77d7e3c14684906525b987961
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/abroot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/abroot.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># abroot

La utilidad ABRoot proporciona inmutabilidad y atomicidad completas al realizar transacciones entre 2 estados de partición raíz (A⟺B).
También permite transacciones bajo demanda a través de un shell transaccional.
Más información: <https://github.com/Vanilla-OS/ABRoot>.

- Muestra el estado actual o futuro de la partición raíz:

`sudo abroot get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">present|future</span>

- Ingresa el shell transaccional en la partición raíz futura y cambia la raíz en el próximo arranque:

`sudo abroot shell`

- Ejecuta un comando específico en el shell transaccional en la futura partición raíz y cambia a él en el siguiente arranque:

`sudo abroot exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Instala paquetes específicos en el host dentro del shell transaccional en la partición raíz futura y cambia a él en el próximo arranque:

`sudo abroot exec apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Actualiza la partición de arranque (solo para usuarios avanzados):

`sudo abroot _update-boot`

- Muestra la ayuda:

`abroot --help`

- Muestra la version:

`abroot --version`
