---
layout: page
title: common/yazi (한국어)
description: "Rust로 작성된 매우 빠른 터미널 파일 관리자."
content_hash: 7b85cac9d39c532827b53c1c7ae85ec26c013ca8
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/yazi.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/yazi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yazi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yazi

Rust로 작성된 매우 빠른 터미널 파일 관리자.
효율적이고 사용자 친화적이며 맞춤형 파일 관리 경험 제공.
더 많은 정보: <https://github.com/sxyazi/yazi>.

- 현재 디렉토리에서 Yazi 시작:

`yazi`

- 디버그 정보 출력:

`yazi --debug`

- 종료 시 현재 작업 디렉토리를 파일에 기록:

`yazi --cwd-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/cwd_파일</span>

- 캐시 디렉토리 비우기:

`yazi --clear-cache`
