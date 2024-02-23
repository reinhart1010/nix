---
layout: page
title: common/fastboot (English)
description: "Communicate with connected Android devices when in bootloader mode (the one place ADB doesn't work)."
content_hash: 5c8c7f0c3565fbd1a1b1c81343fdae47245463ec
last_modified_at: 2024-02-23
related_topics:
  - title: italiano version
    url: /it/common/fastboot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fastboot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fastboot

Communicate with connected Android devices when in bootloader mode (the one place ADB doesn't work).
More information: <https://cs.android.com/android/platform/superproject/+/main:system/core/fastboot>.

- Unlock the bootloader:

`fastboot oem unlock`

- Relock the bootloader:

`fastboot oem lock`

- Reboot the device from fastboot mode into fastboot mode again:

`fastboot reboot bootloader`

- Flash a given image:

`fastboot flash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.img</span>

- Flash a custom recovery image:

`fastboot flash recovery `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.img</span>

- List connected devices:

`fastboot devices`

- Display all information of a device:

`fastboot getvar all`
