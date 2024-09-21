---
layout: page
title: common/btm (한국어)
description: "`top`에 대한 대안."
content_hash: 44a752688f7ce0ee271b4a74981a19e384faaeba
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/btm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/btm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/btm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/btm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># btm

`top`에 대한 대안.
`top`보다 가볍고 크로스 플랫폼이며 그래픽이 더 많이 존재하는 것을 목표로 함.
더 많은 정보: <https://github.com/ClementTsang/bottom>.

- 기본 레이아웃 표시 (CPU, 메모리, 온도, 디스크, 네트워크 및 프로세스):

`btm`

- 기본 모드를 활성화하여, 차트를 제거하고 데이터를 압축 (`top`과 유사):

`btm --basic`

- 차트에 작은 점 대신 큰 점을 사용:

`btm --dot_marker`

- 배터리 충전 및 상태도 표시:

`btm --battery`

- 250 밀리초마다 새로 고치고 차트에 마지막 30초를 표시:

`btm --rate 250 --default_time_value 30000`
