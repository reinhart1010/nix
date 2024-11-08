---
layout: page
title: linux/auditctl (한국어)
description: "Linux 감사 시스템의 동작을 제어하고 상태를 확인하며 규칙을 관리하는 유틸리티."
content_hash: 19b46031865457250f2730c113a39c0bd148314c
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/auditctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/auditctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/auditctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># auditctl

Linux 감사 시스템의 동작을 제어하고 상태를 확인하며 규칙을 관리하는 유틸리티.
더 많은 정보: <https://manned.org/auditctl>.

- 감사 시스템의 [s]상태 표시:

`sudo auditctl -s`

- 현재 로드된 모든 감사 규칙 [l]목록:

`sudo auditctl -l`

- 모든 감사 규칙 [D]삭제:

`sudo auditctl -D`

- 감사 시스템 [e]활성화/비활성화:

`sudo auditctl -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|0</span>

- 파일 변경 감시:

`sudo auditctl -a always,exit -F arch=b64 -F path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/파일</span>` -F perm=wa`

- 디렉토리를 재귀적으로 변경 감시:

`sudo auditctl -a always,exit -F arch=b64 -F dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/폴더/</span>` -F perm=wa`

- [h]도움말 표시:

`auditctl -h`
