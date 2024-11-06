---
layout: page
title: common/hg-log (한국어)
description: "저장소의 수정 내역을 표시."
content_hash: 8cbef8887f71ac630d198d21ea2291844522eec8
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hg-log.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hg-log.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hg log

저장소의 수정 내역을 표시.
더 많은 정보: <https://www.mercurial-scm.org/doc/hg.1.html#log>.

- 저장소의 전체 수정 내역 표시:

`hg log`

- ASCII 그래프와 함께 수정 내역 표시:

`hg log --graph`

- 지정된 패턴과 일치하는 파일 이름과 함께 수정 내역 표시:

`hg log --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 지정된 패턴과 일치하는 파일 이름을 제외한 수정 내역 표시:

`hg log --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 특정 수정에 대한 로그 정보 표시:

`hg log --rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수정</span>

- 특정 브랜치의 수정 내역 표시:

`hg log --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치</span>

- 특정 날짜에 대한 수정 내역 표시:

`hg log --date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">날짜</span>

- 특정 사용자에 의해 커밋된 수정 내역 표시:

`hg log --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>
