---
layout: page
title: common/fastboot (English)
description: "Communicate with connected Android devices when in bootloader mode (the one place `adb` doesn't work)."
content_hash: 7f9677cdb506173709ee2fbce3d7ceb4ea703494
last_modified_at: 2023-11-12
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

Communicate with connected Android devices when in bootloader mode (the one place `adb` doesn't work).
More information: <https://cs.android.com/android/platform/superproject/+/main:system/core/fastboot>.

- Unlock the bootloader:

`fastboot oem unlock`

- Relock the bootloader:

`fastboot oem lock`

- Reboot the device from fastboot mode into fastboot mode again:

`fastboot reboot bootloader`

- Flash a given image:

`fastboot flash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.img</span>

- Flash a custom recovery image:

`fastboot flash recovery `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.img</span>

- Display connected devices:

`fastboot devices`

- Display all information of a device:

`fastboot getvar all`
