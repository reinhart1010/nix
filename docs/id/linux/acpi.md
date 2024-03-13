---
layout: page
title: linux/acpi (Indonesia)
description: "Tampilkan status baterai atau informasi suhu."
content_hash: b22ed5574c6a779ea06c0a9f0ee37be29911ad70
last_modified_at: 2024-03-13
related_topics:
  - title: català version
    url: /ca/linux/acpi.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/acpi.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/acpi.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/acpi.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/acpi.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/acpi.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/acpi.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/acpi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/acpi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># acpi

Tampilkan status baterai atau informasi suhu.
Informasi lebih lanjut: <https://sourceforge.net/projects/acpiclient/files/acpiclient/>.

- Tampilkan informasi baterai:

`acpi`

- Tampilkan informasi suhu:

`acpi -t`

- Tampilkan informasi perangkat pendingin:

`acpi -c`

- Tampilkan informasi suhu dalam Fahrenheit:

`acpi -tf`

- Tampilkan semua informasi:

`acpi -V`

- Ekstrak informasi dari `/proc` daripada `/sys`:

`acpi -p`
