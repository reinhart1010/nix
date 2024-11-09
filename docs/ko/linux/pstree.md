---
layout: page
title: linux/pstree (한국어)
description: "실행 중인 프로세스를 트리 형태로 보여주는 유용한 도구."
content_hash: 2063f86b98878e22f5e772d12aed0aee0ec6aa54
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pstree.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pstree.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pstree

실행 중인 프로세스를 트리 형태로 보여주는 유용한 도구.
더 많은 정보: <https://manned.org/pstree>.

- 프로세스 트리 표시:

`pstree`

- PID와 함께 프로세스 트리 표시:

`pstree -p`

- 특정 사용자가 소유한 프로세스에서 시작하는 모든 프로세스 트리 표시:

`pstree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>
