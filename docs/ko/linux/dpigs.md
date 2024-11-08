---
layout: page
title: linux/dpigs (한국어)
description: "`apt` 기반 시스템에서 설치된 패키지 중 가장 많은 공간을 차지하는 패키지를 표시합니다."
content_hash: 60108490232c156b6ff521a77622d0eae3f3a596
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dpigs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dpigs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dpigs

`apt` 기반 시스템에서 설치된 패키지 중 가장 많은 공간을 차지하는 패키지를 표시합니다.
더 많은 정보: <https://manned.org/dpigs>.

- 시스템에서 가장 큰 N개의 패키지 표시:

`dpigs --lines=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- 기본 dpkg [s]tatus 파일 대신 지정된 [f]파일 사용:

`dpigs --status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 시스템에 설치된 바이너리 패키지의 가장 큰 [S]소스 패키지 표시:

`dpigs --source`

- 패키지 크기를 사람이 읽기 쉬운 [H]형식으로 표시:

`dpigs --human-readable`

- 도움말 표시:

`dpigs --help`
