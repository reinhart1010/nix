---
layout: page
title: common/netserver (한국어)
description: "네트워크 처리량을 측정하는 벤치마킹 애플리케이션 `netperf`의 서버 측 명령."
content_hash: 12a02aa999154e3251d50a014efb998c9b0909f5
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/netserver.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/netserver.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># netserver

네트워크 처리량을 측정하는 벤치마킹 애플리케이션 `netperf`의 서버 측 명령.
같이 보기: `netperf`, 클라이언트 측 명령.
더 많은 정보: <https://manned.org/netserver.1>.

- 기본 포트(12865)에서 서버 시작 및 백그라운드로 포크:

`netserver`

- 포그라운드에서 서버 시작 및 포크하지 않음:

`netserver -D`

- 포트 지정:

`netserver -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- IPv[4] 또는 IPv[6] 강제 설정:

`netserver -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>
