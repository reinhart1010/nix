---
layout: page
title: linux/cpufreq-info (한국어)
description: "CPU 주파수 정보를 표시합니다."
content_hash: 124e42bef56f4c9996994a5e33b279756cd2ed10
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/cpufreq-info.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cpufreq-info

CPU 주파수 정보를 표시합니다.
더 많은 정보: <https://manned.org/cpufreq-info>.

- 모든 CPU의 주파수 정보 표시:

`cpufreq-info`

- 지정된 CPU의 주파수 정보 표시:

`cpufreq-info -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_번호</span>

- 허용된 최소 및 최대 CPU 주파수 표시:

`cpufreq-info -l`

- 현재 최소 및 최대 CPU 주파수와 정책을 표 형식으로 표시:

`cpufreq-info -o`

- 사용 가능한 CPU 주파수 정책 표시:

`cpufreq-info -g`

- cpufreq 커널 모듈에 따라 사람이 읽을 수 있는 형식으로 현재 CPU 작동 주파수 표시:

`cpufreq-info -f -m`

- 하드웨어에서 읽어와 사람이 읽을 수 있는 형식으로 현재 CPU 작동 주파수 표시 (루트 사용자에게만 가능):

`sudo cpufreq-info -w -m`
