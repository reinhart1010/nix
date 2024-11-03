---
layout: page
title: common/pio-device (한국어)
description: "PlatformIO 장치를 관리하고 모니터링."
content_hash: a304d1ad248d4ac3e3becc9a0850187f290557f9
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pio-device.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-device.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio device

PlatformIO 장치를 관리하고 모니터링.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/device/>.

- 사용 가능한 모든 시리얼 포트 나열:

`pio device list`

- 사용 가능한 모든 논리 장치 나열:

`pio device list --logical`

- 대화형 장치 모니터 시작:

`pio device monitor`

- 특정 포트를 수신하며 대화형 장치 모니터 시작:

`pio device monitor --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSBX</span>

- 특정 전송 속도를 설정하여 대화형 장치 모니터 시작 (기본값은 9600):

`pio device monitor --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">57600</span>

- 특정 EOL 문자를 설정하여 대화형 장치 모니터 시작 (기본값은 `CRLF`):

`pio device monitor --eol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CRLF|CR|LF</span>

- 대화형 장치 모니터 메뉴로 이동:

`<Ctrl> + T`
