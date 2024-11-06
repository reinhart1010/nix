---
layout: page
title: common/hg-remove (한국어)
description: "지정된 파일을 스테이징 영역에서 제거."
content_hash: 360347d52a7737f4138d6724cb132e76c006dc30
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hg-remove.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hg-remove.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hg remove

지정된 파일을 스테이징 영역에서 제거.
더 많은 정보: <https://www.mercurial-scm.org/doc/hg.1.html#remove>.

- 파일 또는 디렉토리를 스테이징 영역에서 제거:

`hg remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 패턴과 일치하는 모든 스테이지된 파일 제거:

`hg remove --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 지정된 패턴과 일치하지 않는 모든 스테이지된 파일 제거:

`hg remove --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 하위 저장소를 재귀적으로 제거:

`hg remove --subrepos`

- 물리적으로 제거된 파일을 저장소에서 제거:

`hg remove --after`
