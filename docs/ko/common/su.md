---
layout: page
title: common/su (한국어)
description: "다른 사용자로 쉘을 전환합니다."
content_hash: 69e06d2593238794353f37f8a1889d478600b1ec
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/su.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/su.html
    icon: bi bi-globe
tldri18n_status: 2
---
# su

다른 사용자로 쉘을 전환합니다.
더 많은 정보: <https://manned.org/su>.

- 슈퍼유저로 전환 (루트 비밀번호 필요):

`su`

- 특정 사용자로 전환 (특정 사용자의 비밀번호 필요):

`su `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>

- 특정 사용자로 전환하고 전체 로그인 쉘을 시뮬레이션:

`su - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>

- 다른 사용자로 명령어 실행:

`su - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`
