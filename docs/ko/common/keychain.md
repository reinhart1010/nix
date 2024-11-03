---
layout: page
title: common/keychain (한국어)
description: "ssh-agent 및/또는 gpg-agent를 로그인 간에 재사용."
content_hash: ec69938c85f2a923380e01704188e683afa6532a
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/keychain.html
    icon: bi bi-globe
tldri18n_status: 2
---
# keychain

ssh-agent 및/또는 gpg-agent를 로그인 간에 재사용.
더 많은 정보: <https://funtoo.org/Keychain>.

- 실행 중인 ssh-agent를 확인하고 필요한 경우 시작:

`keychain`

- gpg-agent도 확인:

`keychain --agents "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpg,ssh</span>`"`

- 모든 활성 키의 서명 나열:

`keychain --list`

- 모든 활성 키의 지문 나열:

`keychain --list-fp`

- 에이전트에 추가된 ID에 대한 타임아웃을 분 단위로 추가:

`keychain --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분</span>
