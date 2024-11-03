---
layout: page
title: common/while (한국어)
description: "간단한 셸 루프."
content_hash: 71a7b5a25fdded509ecf1ba60b43b7a401834402
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/while.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/while.html
    icon: bi bi-globe
tldri18n_status: 2
---
# while

간단한 셸 루프.
더 많은 정보: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_04_09>.

- `stdin`을 읽고 각 줄에 대해 작업 수행:

`while read line; do echo "$line"; done`

- 매초마다 명령을 영구적으로 실행:

`while :; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>`; sleep 1; done`
