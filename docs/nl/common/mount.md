---
layout: page
title: common/mount (Nederlands)
description: "Krijg toegang tot een volledig bestandssysteem in één directory."
content_hash: d50762148be20801e6e4e954f02272b9d3667d82
last_modified_at: 2024-08-20
related_topics:
  - title: Deutsch version
    url: /de/common/mount.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mount.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mount.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/mount.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mount.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mount

Krijg toegang tot een volledig bestandssysteem in één directory.
Meer informatie: <https://manned.org/mount.8>.

- Toon alle aangekoppelde bestandssystemen:

`mount`

- Koppel een apparaat aan een directory:

`mount -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandssysteem_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaatbestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/doelmap</span>

- Maak een specifieke directory als deze niet bestaat en koppel een apparaat eraan:

`mount --mkdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaatbestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/doelmap</span>

- Koppel een apparaat aan een directory voor een specifieke gebruiker:

`mount -o uid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker_id</span>`,gid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaatbestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/doelmap</span>

- Koppel een CD-ROM-apparaat (met het bestandstype ISO9660) aan `/cdrom` (alleen-lezen):

`mount -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iso9660</span>` -o ro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/cdrom</span>

- Koppel alle bestandssystemen die zijn gedefinieerd in `/etc/fstab`:

`mount -a`

- Koppel een specifiek bestandssysteem zoals beschreven in `/etc/fstab` (bijv. `/dev/sda1 /my_drive ext2 defaults 0 2`):

`mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/my_drive</span>

- Koppel een directory aan een andere directory:

`mount --bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/oude_map</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/nieuwe_map</span>
