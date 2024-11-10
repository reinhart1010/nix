---
layout: page
title: linux/vcgencmd (한국어)
description: "Raspberry Pi의 시스템 정보를 출력합니다."
content_hash: e58b1106956e454652312ff98b3e3e7c9a04087f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/vcgencmd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vcgencmd

Raspberry Pi의 시스템 정보를 출력합니다.
더 많은 정보: <https://www.raspberrypi.com/documentation/computers/os.html#vcgencmd>.

- 사용 가능한 모든 명령 나열:

`vcgencmd commands`

- 현재 CPU 온도 출력:

`vcgencmd measure_temp`

- 현재 전압 출력:

`vcgencmd measure_volts`

- 시스템의 제한 상태를 비트 패턴으로 출력:

`vcgencmd get_throttled`

- 부트로더 구성 출력 (Raspberry Pi 4 모델에서만 사용 가능):

`vcgencmd bootloader_config`

- 도움말 표시:

`vcgencmd --help`
