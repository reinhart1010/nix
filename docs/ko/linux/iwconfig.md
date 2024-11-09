---
layout: page
title: linux/iwconfig (한국어)
description: "무선 네트워크 인터페이스의 매개변수를 구성하고 표시합니다."
content_hash: 229a256bb6481639b950b1a6c803f36528578331
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/iwconfig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/iwconfig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># iwconfig

무선 네트워크 인터페이스의 매개변수를 구성하고 표시합니다.
더 많은 정보: <https://manned.org/iwconfig>.

- 모든 인터페이스의 매개변수 및 통계 표시:

`iwconfig`

- 특정 인터페이스의 매개변수 및 통계 표시:

`iwconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 특정 인터페이스의 ESSID(네트워크 이름) 설정 (예: eth0 또는 wlp2s0):

`iwconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_네트워크_이름</span>

- 특정 인터페이스의 운영 모드 설정:

`iwconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ad-Hoc|Managed|Master|Repeater|Secondary|Monitor|Auto</span>
