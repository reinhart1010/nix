---
layout: page
title: osx/route (한국어)
description: "수동으로 라우팅 테이블을 조작합니다."
content_hash: 21d31d7b49bf3ce0755a2b1e28d3bffc5fce110b
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/route.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/route.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/route.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/route.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/route.html
    icon: bi bi-globe
tldri18n_status: 2
---
# route

수동으로 라우팅 테이블을 조작합니다.
관리자 권한이 필요합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/route.8.html>.

- 게이트웨이를 통해 대상지로의 경로 추가:

`sudo route add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_IP_주소</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게이트웨이_주소</span>`"`

- 게이트웨이를 통해 /24 서브넷으로의 경로 추가:

`sudo route add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브넷_IP_주소</span>`/24" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게이트웨이_주소</span>`"`

- 테스트 모드로 실행(실행하지 않고 출력만 합니다):

`sudo route -t add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_IP_주소</span>`/24" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게이트웨이_주소</span>`"`

- 모든 경로 제거:

`sudo route flush`

- 특정 경로 삭제:

`sudo route delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_IP_주소</span>`/24"`

- 대상지(호스트명 또는 IP 주소)의 경로 조회 및 표시:

`sudo route get "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>`"`
