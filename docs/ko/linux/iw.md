---
layout: page
title: linux/iw (한국어)
description: "무선 장치를 표시하고 조작."
content_hash: c7e93d69327e498afc7da0ac1ecc5551f08470ad
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/iw.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/iw.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># iw

무선 장치를 표시하고 조작.
같이 보기: `iw dev`.
더 많은 정보: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- 사용 가능한 무선 네트워크 스캔:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` scan`

- 오픈된 무선 네트워크에 연결:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SSID</span>

- 현재 연결 종료:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` disconnect`

- 현재 연결 정보 표시:

`iw dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlp</span>` link`

- 모든 물리적 및 논리적 무선 네트워크 인터페이스 나열:

`iw dev`

- 모든 물리적 하드웨어 인터페이스의 무선 기능 나열:

`iw phy`

- 커널의 현재 무선 규제 도메인 정보 나열:

`iw reg get`

- 모든 명령에 대한 도움말 표시:

`iw help`
