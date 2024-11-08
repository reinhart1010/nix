---
layout: page
title: common/mosquitto_sub (한국어)
description: "주제를 구독하고 수신한 메시지를 출력하는 간단한 MQTT 버전 3.1.1 클라이언트."
content_hash: 321cf668ad4ecba596b7bb17a229824554cb92c6
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mosquitto_sub.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mosquitto_sub

주제를 구독하고 수신한 메시지를 출력하는 간단한 MQTT 버전 3.1.1 클라이언트.
더 많은 정보: <https://mosquitto.org/man/mosquitto_sub-1.html>.

- `sensors/temperature` 주제를 구독하고, 서비스 품질(`QoS`)을 1로 설정합니다. (기본 호스트명은 `localhost`이고 포트는 1883입니다):

`mosquitto_sub -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/temperature</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- `iot.eclipse.org` 포트 1885에서 발행하는 모든 브로커 상태 메시지를 구독하고, 발행된 메시지를 자세히 출력합니다:

`mosquitto_sub -v -h "iot.eclipse.org" -p 1885 -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\$SYS/#</span>

- 주어진 패턴과 일치하는 여러 주제를 구독합니다. (+는 모든 메트릭 이름을 의미합니다):

`mosquitto_sub -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/machines/+/temperature/+</span>
