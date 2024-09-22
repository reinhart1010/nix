---
layout: page
title: common/buku (한국어)
description: "명령어 브라우저 독립적인 북마크 관리자."
content_hash: 3caf7054f765e8d1848a6888f1878273d8ff9c0e
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/buku.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/buku.html
    icon: bi bi-globe
tldri18n_status: 2
---
# buku

명령어 브라우저 독립적인 북마크 관리자.
더 많은 정보: <https://github.com/jarun/Buku>.

- "키워드"와 일치하고 "개인 정보 보호" 태그가 있는 모든 북마크를 표시:

`buku `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>` --stag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개인 정보 보호</span>

- "검색 엔진" 및 "개인 정보 보호" 태그가 포함된 북마크 추가:

`buku --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색 엔진</span>`, `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개인 정보 보호</span>

- 북마크 삭제:

`buku --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">북마크_아이디</span>

- 북마크를 편집하기 위한 편집기 열기:

`buku --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">북마크_아이디</span>

- 북마크에서 "검색 엔진" 태그 제거:

`buku --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">북마크_아이디</span>` --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색 엔진</span>
