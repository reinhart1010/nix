---
layout: page
title: common/mount (italiano)
description: "Fornisce accesso a un intero filesystem in una directory specifica."
content_hash: 1fa94fc7b292e752402cce5741412fd369b36759
related_topics:
  - title: Deutsch version
    url: /de/common/mount.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mount.html
    icon: bi bi-globe
---
# mount

Fornisce accesso a un intero filesystem in una directory specifica.
Maggiori informazioni: <https://manned.org/mount.8>.

- Mostra tutti i filesystem montati:

`mount`

- Monta un dispositivo in una directory:

`mount -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_di_filesystem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/dispositivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_desiderata</span>

- Monta un CD-ROM (con il filetypo ISO9660) a `/cdrom` (sola lettura):

`mount -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iso9660</span>` -o ro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/cdrom</span>

- Monta tutti i filesystem definiti in `/etc/fstab`:

`mount -a`

- Monta un filesystem specifico descritto in `/etc/fstab` (ad esempio `/dev/sda1 /my_drive ext2 defaults 0 2`):

`mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/my_drive</span>

- Monta una directory in un'altra directory:

`mount --bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/vecchia_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/nuova_directory</span>
