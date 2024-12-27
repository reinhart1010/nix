---
layout: page
title: linux/distrobox-export (español)
description: "Exporta aplicaciones/servicios/binarios del contenedor al sistema operativo anfitrión. Vea también: `tldr distrobox`."
content_hash: 5477ecc4a9df4ca97774c398ffefe6eb65e036ac
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/linux/distrobox-export.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/distrobox-export.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-export.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-export

Exporta aplicaciones/servicios/binarios del contenedor al sistema operativo anfitrión. Vea también: `tldr distrobox`.
Más información: <https://distrobox.it/usage/distrobox-export>.

- Exporta una aplicación del contenedor al anfitrión (la entrada de escritorio/ícono aparecerá en la lista de aplicaciones del sistema anfitrión):

`distrobox-export --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>` --extra-flags "--foreground"`

- Exporta un binario del contenedor al anfitrión:

`distrobox-export --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>` --export-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario_en_anfitrión</span>

- Exporta un binario del contenedor al anfitrión (es decir, `$HOME/.local/bin`) :

`distrobox-export --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>` --export-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/exportar</span>

- Exporta un servicio desde el contenedor al anfitrión (`--sudo` ejecutará el servicio como root dentro del contenedor):

`distrobox-export --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>` --extra-flags "--allow-newer-config" --sudo`

- Elimina o deja de exportar una aplicación exportada:

`distrobox-export --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>` --delete`
