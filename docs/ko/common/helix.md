---
layout: page
title: common/helix (한국어)
description: "포스트모던 텍스트 편집기인 Helix는 다양한 종류의 텍스트 조작을 위한 여러 모드를 제공."
content_hash: ed2e43760886ce68060a6f3f3e6ba1542b21c340
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/helix.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/helix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/helix.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># helix

포스트모던 텍스트 편집기인 Helix는 다양한 종류의 텍스트 조작을 위한 여러 모드를 제공.
`i`를 누르면 삽입 모드로 들어감. `<Esc>`는 Helix 명령을 사용할 수 있는 일반 모드로 들어감.
더 많은 정보: <https://helix-editor.com>.

- 파일 열기:

`helix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- Helix 테마 변경:

`:theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테마_이름</span>

- 저장 및 종료:

`:wq<Enter>`

- 저장하지 않고 강제 종료:

`:q!<Enter>`

- 마지막 작업 실행 취소:

`u`

- 파일에서 패턴 검색 (다음/이전 일치 항목으로 이동하려면 `n`/`N`을 누름):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`<Enter>`

- 파일 포맷:

`:format`
