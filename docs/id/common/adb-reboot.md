---
layout: page
title: common/adb-reboot (Indonesia)
description: "Nyalakan ulang suatu perangkat atau emulator Android."
content_hash: 13f9bd61947f842260e12aeea6e34461e80a3df0
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/adb-reboot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adb-reboot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/adb-reboot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># adb reboot

Nyalakan ulang suatu perangkat atau emulator Android.
Informasi lebih lanjut: <https://manned.org/adb>.

- Nyalakan ulang perangkat seperti biasa:

`adb reboot`

- Nyalakan ulang perangkat menuju mode bootloader:

`adb reboot bootloader`

- Nyalakan ulang perangkat menuju mode pemulihan:

`adb reboot recovery`

- Nyalakan ulang perangkat menuju mode fastboot:

`adb reboot fastboot`
