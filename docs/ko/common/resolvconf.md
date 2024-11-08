---
layout: page
title: common/resolvconf (한국어)
description: "네임서버 정보를 관리."
content_hash: 68bc01eb5f647aa9645bf690c26ca70ec9f2b365
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/resolvconf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# resolvconf

네임서버 정보를 관리.
네임서버 정보를 제공하는 프로그램과 이 정보를 사용하는 애플리케이션 사이의 중개 역할을 합니다.
이 페이지는 Debian의 `resolvconf` 구현을 문서화합니다.
더 많은 정보: <https://manned.org/resolvconf.8>.

- IFACE.PROG 레코드를 추가하거나 덮어쓰고 업데이트가 활성화되어 있으면 업데이트 스크립트 실행:

`resolvconf -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IFACE.PROG</span>

- IFACE.PROG 레코드를 삭제하고 업데이트가 활성화되어 있으면 업데이트 스크립트 실행:

`resolvconf -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IFACE.PROG</span>

- 업데이트가 활성화되어 있으면 업데이트 스크립트만 실행:

`resolvconf -u`

- `resolvconf`가 `-a`, `-d`, 또는 `-u`로 호출될 때 업데이트 스크립트를 실행할지 여부를 나타내는 플래그 설정:

`resolvconf --enable-updates`

- 업데이트 실행 여부를 나타내는 플래그 초기화:

`resolvconf --disable-updates`

- 업데이트가 활성화되어 있는지 확인:

`resolvconf --updates-are-enabled`
