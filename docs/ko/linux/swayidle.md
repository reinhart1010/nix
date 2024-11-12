---
layout: page
title: linux/swayidle (한국어)
description: "Wayland용 유휴 관리 데몬."
content_hash: 6b86a63b0e23f895489b87f31692f34adef0125c
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/swayidle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# swayidle

Wayland용 유휴 관리 데몬.
참고: 구성 옵션은 매뉴얼 페이지에 문서화되어 있습니다.
더 많은 정보: <https://github.com/swaywm/swayidle/blob/master/swayidle.1.scd>.

- `$XDG_CONFIG_HOME/swayidle/config` 또는 `$HOME/swayidle/config`에 있는 구성을 사용하여 유휴 활동 수신 대기:

`swayidle`

- 대체 구성 [f]파일 경로 지정:

`swayidle -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
