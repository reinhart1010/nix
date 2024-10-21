---
layout: page
title: common/fold (한국어)
description: "지정된 너비에 맞게 입력 파일의 각 줄을 감싸고 `stdout`으로 출력."
content_hash: 2c478d04291e2a77e973ce5b5a79a414c18e4f50
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/fold.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fold.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fold

지정된 너비에 맞게 입력 파일의 각 줄을 감싸고 `stdout`으로 출력.
더 많은 정보: <https://manned.org/fold.1p>.

- 각 줄을 기본 너비로 변경 (80 자):

`fold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 줄을 너비 "30"으로 줄 바꿈:

`fold -w30 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 줄을 너비 "5"로 묶고 공백에서 줄을 (공백으로 구분된 각 단어를, 새 줄에 넣고, 5보다 큰 단어는 줄바꿈됨):

`fold -w5 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
