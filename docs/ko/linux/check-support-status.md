---
layout: page
title: linux/check-support-status (한국어)
description: "지원이 제한되었거나 조기 종료된 설치된 Debian 패키지를 식별합니다."
content_hash: f589981b41fd7107d10209b47955080ffcac84f9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/check-support-status.html
    icon: bi bi-globe
tldri18n_status: 2
---
# check-support-status

지원이 제한되었거나 조기 종료된 설치된 Debian 패키지를 식별합니다.
더 많은 정보: <https://manned.org/check-support-status>.

- 지원이 제한되었거나 이미 종료되었거나 배포의 수명 종료보다 빨리 종료될 패키지 표시:

`check-support-status`

- 지원이 종료된 패키지만 표시:

`check-support-status --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ended</span>

- 헤드라인 출력 건너뛰기:

`check-support-status --no-heading`
