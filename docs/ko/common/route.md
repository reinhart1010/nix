---
layout: page
title: common/route (한국어)
description: "route 명령어를 사용하여 라우팅 테이블 설정."
content_hash: 46e5a60a17b744982037d010adcb6045cdcb25df
last_modified_at: 2023-10-20
related_topics:
  - title: English version
    url: /en/common/route.html
    icon: bi bi-globe
---
# route

route 명령어를 사용하여 라우팅 테이블 설정.
더 많은 정보: <https://manned.org/route>.

- 라우팅 테이블의 정보를 표시:

`route -n`

- 라우팅 규칙 추가:

`sudo route add -net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피_주소</span>` netmask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">넷마스크_주소</span>` gw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게이트웨이_주소</span>

- 라우팅 규칙 삭제:

`sudo route del -net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피_주소</span>` netmask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">넷마스크_주소</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게이트웨이_주소</span>
