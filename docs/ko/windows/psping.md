---
layout: page
title: windows/psping (한국어)
description: "TCP ping, 대기 시간 및 대역폭 측정을 포함하는 ping 도구입니다."
content_hash: 314ea14203c3ced36f081118fa877e160ce37419
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/windows/psping.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/psping.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># psping

TCP ping, 대기 시간 및 대역폭 측정을 포함하는 ping 도구입니다.
더 많은 정보: <https://learn.microsoft.com/sysinternals/downloads/psping>.

- ICMP를 사용하여 호스트 확인:

`psping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- TCP 포트를 통해 호스트 확인:

`psping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 횟수 지정 및 출력 없이 수행:

`psping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pings</span>` -q`

- TCP를 통해 대상에 50번 ping을 보내고 결과를 히스토그램으로 생성:

`psping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` -q -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` -h`

- 도움말 표시:

`psping /?`
