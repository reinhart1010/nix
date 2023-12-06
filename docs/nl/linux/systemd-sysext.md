---
layout: page
title: linux/systemd-sysext (Nederlands)
description: "Activeer or deactiveer systeem extensie images."
content_hash: 25560da6cd241b710f88281c5196c5859c539d14
last_modified_at: 2023-12-06
related_topics:
  - title: English version
    url: /en/linux/systemd-sysext.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-sysext

Activeer or deactiveer systeem extensie images.
Meer informatie: <https://www.freedesktop.org/software/systemd/man/systemd-sysext.html>.

- Toon geïnstalleerde extensie images:

`systemd-sysext list`

- Voeg systeem extensie images samen in `/usr/` en `/opt/`:

`systemd-sysext merge`

- Toon de huidige status van het samenvoegen:

`systemd-sysext status`

- Draai het samenvoegen van alle huidig geïnstalleerde systeem extensie images terug in `/usr/` en `/opt/`:

`systemd-sysext unmerge`

- Ververs de systeem extensie images (een combinatie van `unmerge` and `merge`):

`systemd-sysext refresh`
