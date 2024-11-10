---
layout: page
title: linux/tlp-stat (한국어)
description: "TLP 상태 보고서 생성."
content_hash: 8be119d7b0970044c666f535a7c34f1fc9694783
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/tlp-stat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlp-stat

TLP 상태 보고서 생성.
같이 보기: `tlp`.
더 많은 정보: <https://linrunner.de/tlp/usage/tlp-stat>.

- 구성 및 모든 활성 설정으로 상태 보고서 생성:

`sudo tlp-stat`

- 다양한 장치에 대한 정보 표시:

`sudo tlp-stat --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">battery|disk|processor|graphics|pcie|rfkill|usb</span>

- 장치에 대해 자세한 정보 표시(자세한 정보 지원 장치만):

`sudo tlp-stat --verbose --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">battery|processor|pcie|usb</span>

- 구성 표시:

`sudo tlp-stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>

- 전원 공급 `udev` 이벤트 모니터링:

`sudo tlp-stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-P|--pev</span>

- 전원 공급 진단 표시:

`sudo tlp-stat --psup`

- 온도 및 팬 속도 표시:

`sudo tlp-stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--temp</span>

- 일반 시스템 정보 표시:

`sudo tlp-stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--system</span>
