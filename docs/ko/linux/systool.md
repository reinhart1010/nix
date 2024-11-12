---
layout: page
title: linux/systool (한국어)
description: "버스 및 클래스별 시스템 장치 정보를 확인합니다."
content_hash: fa631528454067245cfbddc2c209075661dbfb86
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/systool.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/systool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systool

버스 및 클래스별 시스템 장치 정보를 확인합니다.
이 명령어는 `sysfs` 패키지의 일부입니다.
더 많은 정보: <https://github.com/linux-ras/sysfsutils>.

- 버스의 장치 속성을 모두 나열 (예: `pci`, `usb`). 모든 버스를 보려면 `ls /sys/bus` 사용:

`systool -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버스</span>` -v`

- 장치 클래스의 모든 속성을 나열 (예: `drm`, `block`). 모든 클래스를 보려면 `ls /sys/class` 사용:

`systool -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스</span>` -v`

- 버스의 장치 드라이버만 표시 (예: `pci`, `usb`):

`systool -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버스</span>` -D`
