---
layout: page
title: common/calibredb (한국어)
description: "전자책 데이터베이스를 조작하는 도구."
content_hash: 3fccba1ee0ba82d3428107bca873142ce9ffbd34
related_topics:
  - title: English version
    url: /en/common/calibredb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/calibredb.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/calibredb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># calibredb

전자책 데이터베이스를 조작하는 도구.
Calibre 전자책 라이브러리의 일부.
더 많은 정보: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

- 도서관의 전자책들을 추가 정보와 함께 리스트로 출력:

`calibredb list`

- 추가 정보를 표시하며 전자책 검색:

`calibredb list --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_용어</span>

- 전자책의 ID만 검색:

`calibredb search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_용어</span>

- 라이브러리에 전자책 하나 이상 추가하기:

`calibredb add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명1 파일명2 …</span>

- 라이브러리에서 전자책을 하나 이상 제거하기. 전자책 ID 필요(위를 참조하시오):

`calibredb remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id1 id2 …</span>
