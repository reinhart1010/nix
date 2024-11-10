---
layout: page
title: linux/pro (한국어)
description: "Ubuntu Pro 서비스 관리."
content_hash: 319276a97299533aeddd251363e1f526b7ba888d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pro.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pro

Ubuntu Pro 서비스 관리.
더 많은 정보: <https://manned.org/ubuntu-advantage.1>.

- 시스템을 Ubuntu Pro 지원 계약에 연결:

`sudo pro attach`

- Ubuntu Pro 서비스 상태 표시:

`pro status`

- 특정 취약점에 시스템이 영향을 받는지 확인 (가능하다면 수정 적용):

`pro fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CVE-번호</span>

- 지원되지 않는 패키지 수 표시:

`pro security-status`

- 더 이상 다운로드할 수 없는 패키지 나열:

`pro security-status --unavailable`

- 서드파티 패키지 나열:

`pro security-status --thirdparty`
