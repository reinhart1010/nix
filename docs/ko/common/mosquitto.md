---
layout: page
title: common/mosquitto (한국어)
description: "MQTT 브로커."
content_hash: 942441aa8a9e3ef9afef14aa3331ade3564c6e92
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mosquitto.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mosquitto.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mosquitto.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mosquitto

MQTT 브로커.
더 많은 정보: <https://mosquitto.org/>.

- Mosquitto 시작:

`mosquitto`

- 사용할 구성 파일 지정:

`mosquitto --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.conf</span>

- 특정 포트로 수신 대기:

`mosquitto --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8883</span>

- 백그라운드로 포크하여 데몬화:

`mosquitto --daemon`
