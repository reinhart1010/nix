---
layout: page
title: sunos/svcs (한국어)
description: "실행 중인 서비스에 대한 정보를 나열합니다."
content_hash: d2bf34d58d88e0bb438cdd1cd53a03ef8087155d
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/sunos/svcs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/svcs.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/svcs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcs.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/svcs.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svcs

실행 중인 서비스에 대한 정보를 나열합니다.
더 많은 정보: <https://www.unix.com/man-page/linux/1/svcs>.

- 모든 실행 중인 서비스를 나열:

`svcs`

- 실행되고 있지 않은 서비스를 나열:

`svcs -vx`

- 서비스에 대한 정보를 나열:

`svcs apache`

- 서비스 로그 파일의 위치 표시:

`svcs -L apache`

- 서비스 로그 파일의 끝을 표시:

`tail $(svcs -L apache)`
