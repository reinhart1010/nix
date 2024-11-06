---
layout: page
title: common/jps (한국어)
description: "현재 사용자의 JVM 프로세스 상태를 표시."
content_hash: 3cbf0e35c2f43a775dfc4afa1f1cb90022442361
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jps.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/jps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jps

현재 사용자의 JVM 프로세스 상태를 표시.
더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/jps.html>.

- 모든 JVM 프로세스 나열:

`jps`

- PID만 표시하여 모든 JVM 프로세스 나열:

`jps -q`

- 프로세스에 전달된 인수 표시:

`jps -m`

- 모든 프로세스의 전체 패키지 이름 표시:

`jps -l`

- JVM에 전달된 인수 표시:

`jps -v`
