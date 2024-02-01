---
layout: page
title: linux/rpmconf (español)
description: "Gestiona los archivos RPMNEW, RPMSAVE y RPMORIG creados por las actualizaciones de paquetes."
content_hash: 44402b7c990c8d36d755e14c873c2e8620914afd
last_modified_at: 2024-02-01
related_topics:
  - title: English version
    url: /en/linux/rpmconf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rpmconf

Gestiona los archivos RPMNEW, RPMSAVE y RPMORIG creados por las actualizaciones de paquetes.
Vea también: `rpm`.
Más información: <https://github.com/xsuchy/rpmconf>.

- Lista los archivos sobrantes y elige interactivamente que hacer con cada uno de ellos:

`sudo rpmconf --all`

- Elimina los archivos huérfanos RPMNEW y RPMSAVE:

`sudo rpmconf --all --clean`
