---
layout: page
title: common/kak (한국어)
description: "Kakoune는 \"다중 선택\" 패러다임을 구현한 모드 기반 코드 편집기입니다."
content_hash: 6bb0a8fbc84e07464f9e06aa7198c71ab715b9ec
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/kak.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kak

Kakoune는 "다중 선택" 패러다임을 구현한 모드 기반 코드 편집기입니다.
데이터를 여러 위치에서 동시에 선택 및 편집할 수 있으며, 사용자는 동일한 세션에 연결하여 공동 편집을 할 수 있습니다.
더 많은 정보: <https://kakoune.org>.

- 파일을 열고 명령 실행을 위한 일반 모드로 진입:

`kak `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 일반 모드에서 삽입 모드로 전환하여 파일에 텍스트 작성:

`i`

- 삽입 모드를 벗어나 일반 모드로 돌아가기:

`<Esc>`

- 현재 파일에서 "foo"를 모든 "bar"로 대체:

`%s`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`<Enter>c`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>`<Esc>`

- 모든 보조 선택을 해제하고 주 선택만 유지:

`<Space>`

- 숫자를 검색하고 처음 두 개 선택:

`/\d+<Enter>N`

- 파일의 내용을 삽입:

`!cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`<Enter>`

- 현재 파일 저장:

`:w<Enter>`
