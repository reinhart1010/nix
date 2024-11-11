---
layout: page
title: linux/sa (한국어)
description: "사용자가 호출한 명령에 대한 회계 정보를 요약하여 표시하며, 처리에 소비된 CPU 시간 및 I/O 속도에 대한 기본 정보를 포함합니다."
content_hash: 3338552c836f7357bf1530ae2e9e99efc9613ee0
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sa.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sa.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sa

사용자가 호출한 명령에 대한 회계 정보를 요약하여 표시하며, 처리에 소비된 CPU 시간 및 I/O 속도에 대한 기본 정보를 포함합니다.
`acct` 패키지의 일부.
더 많은 정보: <https://manned.org/sa.8>.

- 사용자별 실행 호출 횟수 표시 (사용자명은 표시되지 않음):

`sudo sa`

- 사용자별 실행 호출 횟수 표시, 책임 있는 사용자명 표시:

`sudo sa --print-users`

- 최근 사용자별로 사용된 리소스 목록 표시:

`sudo sa --user-summary`
