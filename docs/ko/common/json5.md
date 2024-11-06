---
layout: page
title: common/json5 (한국어)
description: "JSON5 파일을 JSON으로 변환."
content_hash: c5d72221f780ee6e53460a566daeffd31cc661b5
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/json5.html
    icon: bi bi-globe
tldri18n_status: 2
---
# json5

JSON5 파일을 JSON으로 변환.
더 많은 정보: <https://json5.org>.

- JSON5 `stdin`을 JSON `stdout`으로 변환:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력</span>` | json5`

- JSON5 파일을 JSON으로 변환하여 `stdout`으로 출력:

`json5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.json5</span>

- JSON5 파일을 지정된 JSON 파일로 변환:

`json5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.json5</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.json</span>

- JSON5 파일 유효성 검사:

`json5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.json5</span>` --validate`

- 들여쓰기할 공백 수를 지정 (또는 "t"로 탭 사용):

`json5 --space `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">들여쓰기_수량</span>

- 도움말 표시:

`json5 --help`
