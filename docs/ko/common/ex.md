---
layout: page
title: common/ex (한국어)
description: "명령줄 텍스트 편집기."
content_hash: ca5c74b090b0060891cfef9cf74d3d3cc1e43ad3
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/ex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ex

명령줄 텍스트 편집기.
참고: `vim`.
더 많은 정보: <https://www.vim.org>.

- 파일 열기:

`ex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 저장하고 종료:

`wq<Enter>`

- 마지막 작업 실행 취소:

`undo<Enter>`

- 파일에서 패턴 검색:

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`<Enter>`

- 전체 파일에서 정규식 대체를 수행:

`%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체</span>`/g<Enter>`

- 텍스트 삽입:

`i<Enter>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>`<C-c>`

- Vim으로 전환:

`visual<Enter>`
