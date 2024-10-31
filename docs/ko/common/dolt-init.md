---
layout: page
title: common/dolt-init (한국어)
description: "비어있는 Dolt 데이터 저장소를 생성."
content_hash: 1b3c24845d05b4806a63bc121fe5d2336887e278
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/dolt-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dolt init

비어있는 Dolt 데이터 저장소를 생성.
더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-init>.

- 현재 디렉토리에서 새로운 Dolt 데이터 저장소를 초기화:

`dolt init`

- 지정된 메타데이터로 커밋을 생성하는 새로운 Dolt 데이터 저장소를 초기화:

`dolt init --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`" --email "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일</span>`" --date "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2021-12-31T00:00:00</span>`" -b "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>`"`
