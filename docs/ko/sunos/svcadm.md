---
layout: page
title: sunos/svcadm (한국어)
description: "서비스 인스턴스를 조작합니다."
content_hash: 45794ce7fd18c3775001e3708507de1b44954888
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/sunos/svcadm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/svcadm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/svcadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcadm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/svcadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svcadm

서비스 인스턴스를 조작합니다.
더 많은 정보: <https://www.unix.com/man-page/linux/1m/svcadm>.

- 서비스를 서비스 데이터베이스에서 활성화:

`svcadm enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>

- 서비스 비활성화:

`svcadm disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>

- 실행 중인 서비스 다시 시작:

`svcadm restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>

- 서비스에게 구성 파일을 다시 읽도록 명령:

`svcadm refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>

- 서비스의 유지보수 상태를 해제하고 시작하도록 명령:

`svcadm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>
