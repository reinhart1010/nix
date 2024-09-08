---
layout: page
title: common/airmon-ng (한국어)
description: "무선 네트워크 장치에서 모니터 모드를 활성화."
content_hash: 7fa06d3a78df083ec6b3aa34853c11931f2f25ed
last_modified_at: 2024-09-08
related_topics:
  - title: Deutsch version
    url: /de/common/airmon-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/airmon-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airmon-ng.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airmon-ng.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/airmon-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airmon-ng.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/airmon-ng.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/airmon-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airmon-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airmon-ng

무선 네트워크 장치에서 모니터 모드를 활성화.
`aircrack-ng`의 일부.
더 많은 정보: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- 무선 장치 및 상태를 나열:

`sudo airmon-ng`

- 특정 장치에 대한 모니터 모드 실행:

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- 무선 장치를 사용하는 방해되는 프로세스를 종료:

`sudo airmon-ng check kill`

- 특정 네트워크 인터페이스에 대한 모니터 모드 종료:

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
