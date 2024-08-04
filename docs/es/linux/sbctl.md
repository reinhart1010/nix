---
layout: page
title: linux/sbctl (español)
description: "Un gestor de claves de arranque seguro fácil de usar."
content_hash: 30aa2788c7d56bcda83ab72ab504747424fa338a
last_modified_at: 2024-08-04
related_topics:
  - title: English version
    url: /en/linux/sbctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sbctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sbctl

Un gestor de claves de arranque seguro fácil de usar.
Nota: no registrar los certificados de Microsoft puede bloquear su sistema. Vea <https://github.com/Foxboron/sbctl/wiki/FAQ#option-rom>.
Más información: <https://github.com/Foxboron/sbctl#usage>.

- Muestra el estado actual del arranque seguro:

`sbctl status`

- Crea claves de arranque seguro personalizadas (todo se almacena en `/usr/share/secureboot`):

`sbctl create-keys`

- Inscribe las claves de arranque seguro personalizadas y los certificados de proveedor UEFI de Microsoft:

`sbctl enroll-keys --microsoft`

- Firma un binario EFI con la clave creada y guarda el archivo en la base de datos:

`sbctl sign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--save</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario_efi</span>

- Vuelve a firmar todos los archivos guardados:

`sbctl sign-all`

- Comprueba que se han firmado todos los ejecutables EFI de la partición EFI del sistema:

`sbctl verify`
