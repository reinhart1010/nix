---
layout: page
title: common/esptool.py (한국어)
description: "Espressif 칩용 부트로더 유틸리티 (예: ESP8266)."
content_hash: 02b87e92ca7cd4530af2546446699e4962fc95c3
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/esptool.py.html
    icon: bi bi-globe
tldri18n_status: 2
---
# esptool.py

Espressif 칩용 부트로더 유틸리티 (예: ESP8266).
더 많은 정보: <https://docs.espressif.com/projects/esptool/en/latest/esp32/>.

- 특정 포트 및 전송 속도를 사용하여 펌웨어 파일을 ESP 칩에 플래시:

`sudo esptool.py --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전송_속도</span>` write_flash 0x0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/펌웨어.bin</span>

- ESP 칩의 플래시를 지움:

`sudo esptool.py --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전송_속도</span>` erase_flash`
