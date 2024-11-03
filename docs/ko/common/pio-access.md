---
layout: page
title: common/pio-access (한국어)
description: "레지스트리에 게시된 리소스(패키지)의 접근 수준 설정."
content_hash: 512e3dc869a90f3dd5088bea7dbd46f85cc0a4e0
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pio-access.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-access.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio access

레지스트리에 게시된 리소스(패키지)의 접근 수준 설정.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/access/>.

- 사용자에게 리소스 접근 권한 부여:

`pio access grant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게스트|유지관리자|관리자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_URN</span>

- 사용자의 리소스 접근 권한 제거:

`pio access revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_URN</span>

- 사용자 또는 팀이 접근할 수 있는 모든 리소스와 접근 수준 표시:

`pio access list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 특정 사용자나 팀원에게만 리소스 접근 제한:

`pio access private `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_URN</span>

- 모든 사용자에게 리소스 접근 허용:

`pio access public `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_URN</span>
