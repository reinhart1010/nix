---
layout: page
title: linux/brightnessctl (한국어)
description: "Linux 운영 체제에서 장치 밝기를 읽고 제어하는 유틸리티."
content_hash: e9ab2b534e258be665c447acd6b38e4efdd1fb0f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/brightnessctl.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/brightnessctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/brightnessctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/brightnessctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brightnessctl

Linux 운영 체제에서 장치 밝기를 읽고 제어하는 유틸리티.
더 많은 정보: <https://github.com/Hummer12007/brightnessctl>.

- 밝기를 변경할 수 있는 장치 나열:

`brightnessctl --list`

- 디스플레이 백라이트의 현재 밝기 출력:

`brightnessctl get`

- 디스플레이 백라이트의 밝기를 지정된 범위 내의 백분율로 설정:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50%</span>

- 지정된 증가분만큼 밝기 증가:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+10%</span>

- 지정된 감소분만큼 밝기 감소:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
