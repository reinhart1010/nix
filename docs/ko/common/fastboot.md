---
layout: page
title: common/fastboot (한국어)
description: "부트로더 모드에 있을 때 연결된 Android 장치와 통신 (ADB가 작동하지 않는 곳)."
content_hash: dc232878993f98e88ab7b9bf85f7496cb62ce7d7
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/fastboot.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/fastboot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fastboot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/fastboot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fastboot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fastboot

부트로더 모드에 있을 때 연결된 Android 장치와 통신 (ADB가 작동하지 않는 곳).
더 많은 정보: <https://cs.android.com/android/platform/superproject/+/main:system/core/fastboot>.

- 부트로더 잠금해제:

`fastboot oem unlock`

- 부트로더 리로드:

`fastboot oem lock`

- 장치를 fastboot 모드에서 fastboot 모드로 재부팅:

`fastboot reboot bootloader`

- 주어진 이미지를 조사:

`fastboot flash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.img</span>

- 사용자 정의 복구 이미지 조사:

`fastboot flash recovery `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.img</span>

- 연결된 장치 목록 나열:

`fastboot devices`

- 장치의 모든 정보를 표시:

`fastboot getvar all`
