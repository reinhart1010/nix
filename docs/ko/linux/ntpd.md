---
layout: page
title: linux/ntpd (한국어)
description: "시스템 시계를 원격 시간 서버나 로컬 기준 시계에 동기화하는 공식 NTP(네트워크 시간 프로토콜) 데몬."
content_hash: c9f2fa8fd03a16850fe266cda38a926ef1dc38c5
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/ntpd.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ntpd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ntpd

시스템 시계를 원격 시간 서버나 로컬 기준 시계에 동기화하는 공식 NTP(네트워크 시간 프로토콜) 데몬.
더 많은 정보: <https://manned.org/ntpd>.

- 데몬 시작:

`sudo ntpd`

- 시스템 시간을 원격 서버와 한 번 동기화(동기화 후 종료):

`sudo ntpd --quit`

- "큰" 조정을 허용하여 한 번 동기화:

`sudo ntpd --panicgate --quit`
