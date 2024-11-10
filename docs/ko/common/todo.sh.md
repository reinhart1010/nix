---
layout: page
title: common/todo.sh (한국어)
description: "`todo.txt` 파일을 관리하기 위한 간단하고 확장 가능한 셸 스크립트."
content_hash: c3341497dbf249e65ac1afaba0ec165f82c95003
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/todo.sh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# todo.sh

`todo.txt` 파일을 관리하기 위한 간단하고 확장 가능한 셸 스크립트.
더 많은 정보: <https://github.com/todotxt/todo.txt-cli>.

- 모든 항목 나열:

`todo.sh ls`

- 프로젝트 및 컨텍스트 태그로 항목 추가:

`todo.sh add '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설명</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨텍스트</span>`'`

- 항목을 [완료]로 표시:

`todo.sh do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_번호</span>

- 항목 제거:

`todo.sh rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_번호</span>

- 항목의 [우선순위] 설정 (A-Z):

`todo.sh pri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">우선순위</span>

- 항목 교체:

`todo.sh replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_번호</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_설명</span>`'`
