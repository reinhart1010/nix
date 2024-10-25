---
layout: page
title: linux/sbctl (español)
description: "Un gestor de claves de arranque seguro fácil de usar."
content_hash: 1e254eb940a61d26685e33a814ec13c6bbb4011f
last_modified_at: 2024-10-25
related_topics:
  - title: English version
    url: /en/linux/sbctl.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sbctl

Un gestor de claves de arranque seguro fácil de usar.
Nota: no registrar los certificados de Microsoft puede bloquear su sistema. Ver <https://github.com/Foxboron/sbctl/wiki/FAQ#option-rom>.
Más información: <https://github.com/Foxboron/sbctl#usage>.

- Muestra el estado actual del arranque seguro:

`sbctl status`

- Crea claves de arranque seguro personalizadas (todo se almacena en `/var/lib/sbctl` de forma predeterminada):

`sbctl create-keys`

- Inscribe las claves de arranque seguro personalizadas y los certificados de proveedor UEFI:

`sbctl enroll-keys --microsoft`

- Ejecuta automáticamente `create-keys` y `enroll-keys` basado en los parámetros de `/etc/sbctl/sbctl.conf`:

`sbctl setup --setup`

- Firma un binario EFI con la clave creada y guarda el archivo en la base de datos:

`sbctl sign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--save</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario_efi</span>

- Vuelve a firmar todos los archivos guardados:

`sbctl sign-all`

- Comprueba que se han firmado todos los ejecutables EFI de la partición EFI del sistema:

`sbctl verify`
