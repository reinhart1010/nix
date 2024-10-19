---
layout: page
title: common/adb-reboot (中文)
description: "重启已连接的 Android 设备或模拟器。"
content_hash: e50992f9bb4d1e72ef25d030a4c8cffe0cf46fee
last_modified_at: 2024-10-19
related_topics:
  - title: English version
    url: /en/common/adb-reboot.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-reboot.html
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

重启已连接的 Android 设备或模拟器。
更多信息：<https://manned.org/adb>.

- 正常重启设备:

`adb reboot`

- 重启设备到引导加载程序模式:

`adb reboot bootloader`

- 重启设备到恢复模式:

`adb reboot recovery`

- 重启设备到 fastboot 模式:

`adb reboot fastboot`
