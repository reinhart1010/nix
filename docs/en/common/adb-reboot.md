---
layout: page
title: common/adb-reboot (English)
description: "Reboot a connected Android device or emulator."
content_hash: af68840df47bc1c9be1821cf23ea095fae138696
last_modified_at: 2024-10-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/adb-reboot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># adb reboot

Reboot a connected Android device or emulator.
More information: <https://manned.org/adb>.

- Reboot the device normally:

`adb reboot`

- Reboot the device into bootloader mode:

`adb reboot bootloader`

- Reboot the device into recovery mode:

`adb reboot recovery`

- Reboot the device into fastboot mode:

`adb reboot fastboot`
