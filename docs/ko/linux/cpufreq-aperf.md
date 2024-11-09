---
layout: page
title: linux/cpufreq-aperf (한국어)
description: "일정 시간 동안 평균 CPU 주파수를 계산합니다."
content_hash: f3b801aa38bedb0c106d24be0374461f627e37b0
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/cpufreq-aperf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cpufreq-aperf

일정 시간 동안 평균 CPU 주파수를 계산합니다.
루트 권한이 필요합니다.
더 많은 정보: <https://manned.org/cpufreq-aperf>.

- 모든 CPU 코어와 1초 새로고침 간격으로 계산 시작:

`sudo cpufreq-aperf`

- CPU 1만 계산 시작:

`sudo cpufreq-aperf -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 모든 CPU 코어에 대해 3초 새로고침 간격으로 계산 시작:

`sudo cpufreq-aperf -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- 한 번만 계산:

`sudo cpufreq-aperf -o`
