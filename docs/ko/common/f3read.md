---
layout: page
title: common/f3read (한국어)
description: ".h2w 파일을 검증하여 드라이브의 실제 용량을 테스트."
content_hash: b44f3beb9c2085f020cbdbdd9647769c7770f595
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/f3read.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/f3read.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># f3read

.h2w 파일을 검증하여 드라이브의 실제 용량을 테스트.
참고: `f3write`, `f3probe`, `f3fix`.
더 많은 정보: <https://oss.digirati.com.br/f3/>.

- 특정 디렉터리의 파일을 확인하여, 장치의 유효성을 검사:

`f3read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>
