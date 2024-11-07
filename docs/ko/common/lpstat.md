---
layout: page
title: common/lpstat (한국어)
description: "프린터에 대한 상태 정보를 표시."
content_hash: 74f8e97a06a115696a97c0b3d638215890461dea
last_modified_at: 2024-11-07
related_topics:
  - title: Deutsch version
    url: /de/common/lpstat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/lpstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/lpstat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lpstat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lpstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lpstat

프린터에 대한 상태 정보를 표시.
더 많은 정보: <https://manned.org/lpstat>.

- 기기에 존재하는 프린터와 프린터 사용 가능 여부 나열:

`lpstat -p`

- 기본 프린터 표시:

`lpstat -d`

- 사용 가능한 모든 상태 정보 표시:

`lpstat -t`

- 특정 사용자가 대기 중인 인쇄 작업 나열:

`lpstat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>
