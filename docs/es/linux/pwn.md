---
layout: page
title: linux/pwn (español)
description: "Biblioteca de desarrollo de exploits diseñada para la creación rápida de prototipos."
content_hash: 956974114f66fea050de11240eb70a78d5ef6987
last_modified_at: 2024-03-04
related_topics:
  - title: English version
    url: /en/linux/pwn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pwn

Biblioteca de desarrollo de exploits diseñada para la creación rápida de prototipos.
Más información: <https://docs.pwntools.com/en/stable/commandline.html>.

- Convierte código ensamblador a `bytes`:

`pwn asm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xor edi, edi</span>`"`

- Crea un patrón cíclico con un número específico de caracteres:

`pwn cyclic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>

- Codifica datos en el sistema hexadecimal:

`pwn hex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deafbeef</span>

- Decodifica datos en hexadecimal:

`pwn unhex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6c4f7645</span>

- Imprime código de intérprete de Linux x64 para ejecutar en un intérprete:

`pwn shellcraft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">amd64.linux.sh</span>

- Comprueba la configuración de seguridad binaria del archivo ELF dado:

`pwn checksec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Busca actualizaciones de Pwntools:

`pwn update`

- Muestra la versión:

`pwn version`
