---
layout: page
title: common/seq (한국어)
description: "숫자 시퀀스를 `stdout`에 출력."
content_hash: 62bf135f4f192c5c0e157fd78d8135e665e8e491
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/seq.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/seq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# seq

숫자 시퀀스를 `stdout`에 출력.
더 많은 정보: <https://www.gnu.org/software/coreutils/seq>.

- 1부터 10까지의 시퀀스:

`seq 10`

- 5부터 20까지 3씩 증가하는 숫자:

`seq 5 3 20`

- 출력 항목을 줄바꿈 대신 공백으로 구분:

`seq -s " " 5 3 20`

- 출력 너비를 최소 4자리로 맞추고 필요한 경우 0으로 채움:

`seq -f "%04g" 5 3 20`
