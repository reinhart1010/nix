---
layout: page
title: common/mount (Deutsch)
description: "Ermöglicht den Zugriff auf ein gesamtes Dateisystem in einem Verzeichnis."
content_hash: 1029b55ff4ab5d290c25b3d9aded128ec6812108
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/mount.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mount.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/mount.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mount

Ermöglicht den Zugriff auf ein gesamtes Dateisystem in einem Verzeichnis.
Weitere Informationen: <https://manned.org/mount.8>.

- Zeige alle eingehängten Dateisysteme:

`mount`

- Hänge ein Gerät in ein Verzeichnis ein:

`mount -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateisystemtyp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/gerätedatei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/zielverzeichnis</span>

- Hänge ein CD-ROM-Gerät (Dateisystemtyp ISO9660) in das Verzeichnis `/cdrom` schreibgeschützt ein:

`mount -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iso9660</span>` -o ro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/cdrom</span>

- Hänge alle Dateisysteme ein, die in `/etc/fstab` definiert sind:

`mount -a`

- Hänge ein Dateisystem ein, das in `/etc/fstab` beschrieben ist (z. B. `/dev/sda1 /meine_platte ext2 defaults 0 2`):

`mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/meine_platte</span>

- Hänge ein Verzeichnis in ein anderes Verzeichnis ein (danach sind die Inhalte über beide Pfade verfügbar):

`mount --bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/altem_verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/neuem_verzeichnis</span>
