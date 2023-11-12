---
layout: page
title: linux/rig (español)
description: "Utilidad para generar un nombre, apellido, calle y número, junto a ubicación geográfica consistente (un conjunto válido de ciudad, estado y código postal)."
content_hash: 888400b070e116fc568f65899bce8e31ac8c62b8
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/rig.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/rig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rig

Utilidad para generar un nombre, apellido, calle y número, junto a ubicación geográfica consistente (un conjunto válido de ciudad, estado y código postal).
Más información: <https://manned.org/rig>.

- Muestra un nombre aleatorio (masculino o femenino) y una dirección:

`rig`

- Muestra un nombre [m]asculino, (o [f]emenino) aleatorio y una dirección:

`rig -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">m|f</span>

- Usa archivos de datos de un directorio específico (por defecto es `/usr/share/rig`):

`rig -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Especifica el número de identidades a generar:

`rig -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero</span>

- Especifica el número de identidades femininas a generar:

`rig -f -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero</span>
