---
layout: page
title: linux/pidstat (한국어)
description: "CPU, 메모리, IO 등 시스템 리소스 사용량을 표시합니다."
content_hash: 913f75b82e6e26e61b322d6b6d68e6eb38655ad7
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pidstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pidstat

CPU, 메모리, IO 등 시스템 리소스 사용량을 표시합니다.
더 많은 정보: <https://manned.org/pidstat>.

- 2초 간격으로 10회 CPU 통계 표시:

`pidstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 페이지 폴트 및 메모리 사용량 표시:

`pidstat -r`

- 프로세스 ID별 입출력 사용량 표시:

`pidstat -d`

- 특정 PID에 대한 정보 표시:

`pidstat -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- 명령 이름에 "fox" 또는 "bird"가 포함된 모든 프로세스의 메모리 통계 표시:

`pidstat -C "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fox|bird</span>`" -r -p ALL`
