---
layout: page
title: linux/turbostat (한국어)
description: "프로세서 토폴로지, 주파수, 온도, 전력 및 유휴 통계를 보고합니다."
content_hash: 05c066469ec56b815b3905c349b60ef953b71791
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/turbostat.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/turbostat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# turbostat

프로세서 토폴로지, 주파수, 온도, 전력 및 유휴 통계를 보고합니다.
더 많은 정보: <https://manned.org/turbostat.8>.

- 5초마다 통계 표시:

`sudo turbostat`

- 지정한 초마다 통계 표시:

`sudo turbostat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>

- 시스템 구성 헤더 정보를 해독하여 출력하지 않음:

`sudo turbostat --quiet`

- 헤더 정보 없이 1초마다 CPU에 대한 유용한 정보 표시:

`sudo turbostat --quiet --interval 1 --cpu 0-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CPU_스레드_수</span>` --show "PkgWatt","Busy%","Core","CoreTmp","Thermal"`

- 도움말 표시:

`turbostat --help`
