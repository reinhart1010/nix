---
layout: page
title: linux/sic (한국어)
description: "Simple IRC 클라이언트."
content_hash: 1577310017eedb9eed9712067eeae1ab158251a8
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/sic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sic

Simple IRC 클라이언트.
suckless 도구의 일부.
더 많은 정보: <https://tools.suckless.org/sic/>.

- 기본 호스트(irc.ofct.net)에 `$USER` 환경 변수에 설정된 닉네임으로 연결:

`sic`

- 주어진 호스트에 주어진 닉네임으로 연결:

`sic -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">닉네임</span>

- 주어진 호스트에 주어진 닉네임과 비밀번호로 연결:

`sic -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">닉네임</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 채널 참여:

`:j #`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">채널</span>`<Enter>`

- 채널이나 사용자에게 메시지 전송:

`:m #`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">채널|사용자</span>`<Enter>`

- 기본 채널이나 사용자 설정:

`:s #`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">채널|사용자</span>`<Enter>`
