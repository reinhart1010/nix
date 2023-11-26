---
layout: page
title: osx/tmutil (español)
description: "Utilidad para gestionar las copias de seguridad de Time Machine. La mayoría de las acciones requieren privilegios de root."
content_hash: 5d36030db81dda0750fd887ddf9821e8923c8c0a
last_modified_at: 2023-11-26
related_topics:
  - title: Deutsch version
    url: /de/osx/tmutil.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/tmutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tmutil

Utilidad para gestionar las copias de seguridad de Time Machine. La mayoría de las acciones requieren privilegios de root.
Más información: <https://ss64.com/osx/tmutil.html>.

- Establece una unidad HFS+ como destino de la copia de seguridad:

`sudo tmutil setdestination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/punto_montaje_disco</span>

- Establece un recurso compartido APF o SMB como destino de la copia de seguridad:

`sudo tmutil setdestination "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocolo://usuario[:contraseña]@host/compartir</span>`"`

- Añade el destino indicado a la lista de destinos:

`sudo tmutil setdestination -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>

- Activa copias de seguridad automáticas:

`sudo tmutil enable`

- Desactiva las copias de seguridad automáticas:

`sudo tmutil disable`

- Inicia una copia de seguridad, si ya no se está ejecutando, y libera el control del intérprete de comandos:

`sudo tmutil startbackup`

- Inicia una copia de seguridad y bloquearla hasta que termine:

`sudo tmutil startbackup -b`

- Detiene una copia de seguridad:

`sudo tmutil stopbackup`
