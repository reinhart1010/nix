---
layout: page
title: linux/fatrace (한국어)
description: "파일 접근 이벤트 보고."
content_hash: 9e016d4c8c8e11baf282c008c6529f2530b93b8a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/fatrace.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fatrace.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fatrace

파일 접근 이벤트 보고.
더 많은 정보: <https://manned.org/fatrace>.

- 모든 마운트된 파일시스템의 파일 접근 이벤트를 `stdout`에 출력:

`sudo fatrace`

- 현재 디렉토리의 마운트에서 파일 접근 이벤트를 타임스탬프와 함께 `stdout`에 출력:

`sudo fatrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--current-mount</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--timestamp</span>
