---
layout: page
title: common/ntpctl (한국어)
description: "실행 중인 OpenNTPD 인스턴스에 대한 정보를 표시."
content_hash: 6158567e9c4f1588e0b46780cdc97e9a57bc9091
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ntpctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ntpctl

실행 중인 OpenNTPD 인스턴스에 대한 정보를 표시.
더 많은 정보: <https://man.openbsd.org/ntpctl>.

- 모든 데이터 표시:

`ntpctl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|all</span>

- 각 피어에 대한 정보 표시:

`ntpctl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">p|peers</span>

- 피어와 센서의 상태 및 시스템 시계 동기화 여부 표시:

`ntpctl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|status</span>

- 각 센서에 대한 정보 표시:

`ntpctl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">S|Sensors</span>
