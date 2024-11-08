---
layout: page
title: common/mosquitto_pub (한국어)
description: "단일 메시지를 주제에 게시하고 종료하는 간단한 MQTT 버전 3.1.1 클라이언트."
content_hash: dc74eda3e8be07658bc88aea5bc19b6a237d4741
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mosquitto_pub.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mosquitto_pub

단일 메시지를 주제에 게시하고 종료하는 간단한 MQTT 버전 3.1.1 클라이언트.
더 많은 정보: <https://mosquitto.org/man/mosquitto_pub-1.html>.

- Quality of Service(QoS)를 1로 설정하고, 192.168.1.1(기본값은 `localhost`)에 `sensors/temperature` 주제로 온도 값 32 게시:

`mosquitto_pub -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/temperature</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">32</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 비표준 포트로 원격 호스트에 `sensors/temperature` 주제로 타임스탬프와 온도 데이터 게시:

`mosquitto_pub -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1885</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/temperature</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1266193804 32</span>`"`

- 스위치 이벤트 사이에 긴 시간이 있을 수 있으므로, 원격 호스트에 `switches/kitchen_lights/status` 주제로 스위치 상태 게시 및 메시지 유지:

`mosquitto_pub -r -h "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iot.eclipse.org</span>`" -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">switches/kitchen_lights/status</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on</span>`"`

- 파일(`data.txt`)의 내용을 메시지로 전송하고 `sensors/temperature` 주제로 게시:

`mosquitto_pub -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/temperature</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.txt</span>

- `stdin`에서 읽어들인 파일(`data.txt`)의 전체 입력 내용을 메시지로 전송하고 `sensors/temperature` 주제로 게시:

`mosquitto_pub -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/temperature</span>` -s < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.txt</span>

- `stdin`에서 줄바꿈된 데이터를 메시지로 읽어들여 `sensors/temperature` 주제로 게시:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo data.txt</span>` | mosquitto_pub -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/temperature</span>` -l`
