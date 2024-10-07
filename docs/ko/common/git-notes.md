---
layout: page
title: common/git-notes (한국어)
description: "객체 노트를 추가하거나 검사."
content_hash: c8c077a308bee38733c002d30968d7ec7d102ae0
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-notes.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-notes.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-notes.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-notes.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git notes

객체 노트를 추가하거나 검사.
더 많은 정보: <https://git-scm.com/docs/git-notes>.

- 모든 노트와 연결된 객체 나열:

`git notes list`

- 주어진 객체에 연결된 모든 노트 나열 (기본값은 HEAD):

`git notes list [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체</span>`]`

- 주어진 객체에 연결된 노트 표시 (기본값은 HEAD):

`git notes show [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체</span>`]`

- 지정된 객체에 노트 추가 (기본 텍스트 편집기 열림):

`git notes append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체</span>

- 지정된 객체에 메시지를 지정하여 노트 추가:

`git notes append --message="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지_텍스트</span>`"`

- 기존 노트 편집 (기본값은 HEAD):

`git notes edit [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체</span>`]`

- 한 객체에서 다른 객체로 노트 복사:

`git notes copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_객체</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_객체</span>

- 지정된 객체에 추가된 모든 노트 제거:

`git notes remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체</span>
