---
layout: page
title: linux/iwlist (한국어)
description: "무선 인터페이스에서 자세한 정보 가져오기."
content_hash: da3c6a25fbe518ee20dcd8a74770f2f1bb2af164
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/iwlist.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/iwlist.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/iwlist.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># iwlist

무선 인터페이스에서 자세한 정보 가져오기.
더 많은 정보: <https://manned.org/iwlist.8>.

- 범위 내 액세스 포인트 및 애드혹 셀 목록 표시:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">무선_인터페이스</span>` scan`

- 장치에서 사용 가능한 주파수 표시:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">무선_인터페이스</span>` frequency`

- 장치가 지원하는 비트 전송률 나열:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">무선_인터페이스</span>` rate`

- 현재 설정된 WPA 인증 매개변수 나열:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">무선_인터페이스</span>` auth`

- 장치에 설정된 모든 WPA 암호화 키 나열:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">무선_인터페이스</span>` wpakeys`

- 지원되는 암호화 키 크기 및 장치에 설정된 모든 암호화 키 나열:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">무선_인터페이스</span>` keys`

- 장치의 다양한 전원 관리 속성과 모드 나열:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">무선_인터페이스</span>` power`

- 장치에 설정된 일반 정보 요소 나열(WPA 지원에 사용됨):

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">무선_인터페이스</span>` genie`
