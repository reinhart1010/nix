---
layout: page
title: linux/alien (한국어)
description: "다양한 설치 패키지를 다른 형식으로 변환합니다."
content_hash: a15fb17339b7d6753511ae15e3c2b8adfa9db4e2
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/alien.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/alien.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/alien.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/alien.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/alien.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/alien.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/alien.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alien

다양한 설치 패키지를 다른 형식으로 변환합니다.
같이 보기: `debtap`, Arch Linux에서 `.deb` 변환을 위한 도구.
더 많은 정보: <https://manned.org/alien>.

- 특정 설치 파일을 Debian 형식(`.deb` 확장자)으로 변환:

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 설치 파일을 Red Hat 형식(`.rpm` 확장자)으로 변환:

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 설치 파일을 Slackware 설치 파일(`.tgz` 확장자)로 변환:

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 설치 파일을 Debian 형식으로 변환하고 시스템에 설치:

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
