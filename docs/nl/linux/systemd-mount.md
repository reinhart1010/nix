---
layout: page
title: linux/systemd-mount (Nederlands)
description: "Zet mount of auto-mount punten op of verwijder ze."
content_hash: 24a33bcc1e9874b2cb7f4420103889d0e392af16
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/linux/systemd-mount.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-mount.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-mount

Zet mount of auto-mount punten op of verwijder ze.
Meer informatie: <https://www.freedesktop.org/software/systemd/man/systemd-mount.html>.

- Mount een bestandssysteem (afbeelding of blokapparaat) op `/run/media/system/LABEL` waar LABEL het bestandssysteemlabel is of de apparaatnaam als er geen label is:

`systemd-mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_apparaat</span>

- Mount een bestandssysteem (afbeelding of blokapparaat) op een gegeven locatie:

`systemd-mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_apparaat</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/mount_point</span>

- Toon een lijst van alle lokale, bekende blokapparaten met de bestandssystemen die mogelijk gemount kunnen worden:

`systemd-mount --list`

- Maak een automount punt dat het bestandssysteem zal mounten op het moment van eerste toegang:

`systemd-mount --automount=yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_apparaat</span>

- Unmount een of meerdere apparaten:

`systemd-mount --umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/mount_point_of_apparaat1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/mount_point_of_apparaat2</span>

- Mount een bestandssysteem (afbeelding of blokapparaat) met een specifiek bestandssysteemtype:

`systemd-mount --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_system_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_apparaat</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/mount_point</span>

- Mount een bestandssysteem (afbeelding of blokapparaat) met extra mount opties:

`systemd-mount --options=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mount_options</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_apparaat</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/mount_point</span>
