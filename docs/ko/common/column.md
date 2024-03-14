---
layout: page
title: common/column (한국어)
description: "표준 입력 또는 파일을 여러 열로 포맷 설정."
content_hash: f60d2a67b2d04d1e7f292b50f735467337a0d7a6
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/column.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/column.html
    icon: bi bi-globe
tldri18n_status: 2
---
# column

표준 입력 또는 파일을 여러 열로 포맷 설정.
행 앞에 열이 채워짐; 기본 구분 기호는 공백입니다.
더 많은 정보: <https://manned.org/column>.

- 30자 폭 디스플레이의 형식 출력으로 포맷 정하기:

`printf "header1 header2\nbar foo\n" | column --output-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- 열 자동 분할 및 자동 정렬을 표 형식으로 분할:

`printf "header1 header2\nbar foo\n" | column --table`

- -t 옵션(예: "", CSV)에 대한 열 구분 기호 문자를 지정; 기본값은 공백입니다:

`printf "header1,header2\nbar,foo\n" | column --table --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- 열을 채우기 전에 행 채우기:

`printf "header1\nbar\nfoobar\n" | column --output-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` --fillrows`
