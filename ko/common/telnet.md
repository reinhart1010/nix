---
layout: page
title: common/telnet (한국어)
description: "telnet 프로토콜을 사용해 호스트의 특정 포트에 연결합니다."
content_hash: 7806f82f4b4d3602d6bd25600e55d38e17fd6d5c
related_topics:
  - title: English version
    url: /en/common/telnet.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># telnet

telnet 프로토콜을 사용해 호스트의 특정 포트에 연결합니다.
더 많은 정보: <https://manned.org/telnet>.

- 호스트의 기본 포트에 Telnet 연결:

`telnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 호스트의 특정 포트에 Telnet 연결:

`telnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- Telnet 세션 종료:

`quit`

- 세션 종료를 위한 기본 이스케이프 문자 조합을 전송:

`Ctrl + ]`

- "x"를 세션 종료 문자로 사용하여 세션 시작:

`telnet -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- Telnet 으로 스타워즈 보기:

`telnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">towel.blinkenlights.nl</span>
