---
layout: page
title: linux/kpackagetool6 (español)
description: "KPackage Manager: instala, lista, elimina paquetes Plasma."
content_hash: 78077bce6027e44ed9dea6c262c045bdd4242da5
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/kpackagetool6.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kpackagetool6

KPackage Manager: instala, lista, elimina paquetes Plasma.
Más información: <https://manned.org/kpackagetool6>.

- Lista todos los tipos de paquetes conocidos que se pueden instalar:

`kpackagetool6 --list-types`

- Instala el paquete desde un directorio:

`kpackagetool6 --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_paquete</span>` --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>

- Actualiza el paquete instalado desde un directorio:

`kpackagetool6 --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_paquete</span>` --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>

- Lista los plasmoides instalados (`--global` para todos los usuarios):

`kpackagetool6 --type Plasma/Applet --list --global`

- Elimina un plasmoide por su nombre:

`kpackagetool6 --type Plasma/Applet --remove "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>`"`
