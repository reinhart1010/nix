---
layout: page
title: linux/ddcutil (한국어)
description: "DDC/CI를 통해 연결된 디스플레이의 설정을 제어합니다."
content_hash: 17d84d3f9258c9c3325188a1e52ad740644a6e10
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/ddcutil.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ddcutil.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ddcutil

DDC/CI를 통해 연결된 디스플레이의 설정을 제어합니다.
이 명령은 `i2c-dev` 커널 모듈이 로드되어 있어야 합니다. 같이 보기: `modprobe`.
더 많은 정보: <https://www.ddcutil.com>.

- 호환 가능한 모든 디스플레이 나열:

`ddcutil detect`

- 디스플레이 1의 밝기(옵션 0x10)를 50%로 변경:

`ddcutil --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` setvcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- 디스플레이 1의 대비(옵션 0x12)를 5% 증가:

`ddcutil -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` setvcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 디스플레이 1의 설정 읽기:

`ddcutil -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` getvcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ALL</span>
