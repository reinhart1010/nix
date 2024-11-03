---
layout: page
title: common/pio-system (한국어)
description: "PlatformIO의 다양한 시스템 명령."
content_hash: 4279062f73851ad5e91b5cfda045bd6f6b6dbb1c
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pio-system.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-system.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio system

PlatformIO의 다양한 시스템 명령.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/system/>.

- 현재 셸에 대한 셸 자동 완성 설치 (Bash, fish, Zsh 및 PowerShell 지원):

`pio system completion install`

- 현재 셸에 대한 셸 자동 완성 제거:

`pio system completion uninstall`

- 시스템 전역 PlatformIO 정보 표시:

`pio system info`

- 사용하지 않는 PlatformIO 데이터 제거:

`pio system prune`

- 캐시된 데이터만 제거:

`pio system prune --cache`

- 제거될 사용하지 않는 PlatformIO 데이터를 목록으로 표시하지만 실제로 제거하지 않음:

`pio system prune --dry-run`
