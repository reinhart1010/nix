---
layout: page
title: common/adb-reboot (한국어)
description: "연결된 Android 기기 또는 에뮬레이터를 재부팅."
content_hash: f6bbd481fe2eaa0bcb0d7a3bc82dcf72525ee370
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/adb-reboot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/adb-reboot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># adb reboot

연결된 Android 기기 또는 에뮬레이터를 재부팅.
더 많은 정보: <https://manned.org/adb>.

- 장치를 정상적으로 재부팅:

`adb reboot`

- 장치를 부트로더 모드로 재부팅:

`adb reboot bootloader`

- 장치를 복구 모드로 재부팅:

`adb reboot recovery`

- 장치를 빠른 부팅 모드로 재부팅:

`adb reboot fastboot`
