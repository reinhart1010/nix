---
layout: page
title: common/hg-commit (한국어)
description: "준비된 모든 파일 또는 지정된 파일을 저장소에 커밋."
content_hash: db8de2e412bcf88cb19e0c4ed259dd753f5cf272
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hg-commit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hg-commit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hg commit

준비된 모든 파일 또는 지정된 파일을 저장소에 커밋.
더 많은 정보: <https://www.mercurial-scm.org/doc/hg.1.html#commit>.

- 준비된 파일을 저장소에 커밋:

`hg commit`

- 특정 파일 또는 디렉터리를 커밋:

`hg commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 특정 메시지와 함께 커밋:

`hg commit --message `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>

- 지정된 패턴과 일치하는 모든 파일을 커밋:

`hg commit --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 지정된 패턴과 일치하지 않는 모든 파일을 커밋:

`hg commit --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 대화형 모드를 사용하여 커밋:

`hg commit --interactive`
