---
layout: page
title: common/auditd (한국어)
description: "감사 유틸리티의 요청과 커널의 알림에 응답합니다."
content_hash: 83a16f6800fad98ed0dd99ea078104b14f3b2674
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/auditd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/auditd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/auditd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># auditd

감사 유틸리티의 요청과 커널의 알림에 응답합니다.
수동으로 호출해서는 안 됩니다.
더 많은 정보: <https://manned.org/auditd>.

- 데몬 시작:

`auditd`

- 디버그 모드에서 데몬 시작:

`auditd -d`

- launchd에서 주문형 데몬 시작:

`auditd -l`
