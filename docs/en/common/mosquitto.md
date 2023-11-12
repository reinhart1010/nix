---
layout: page
title: common/mosquitto (English)
description: "An MQTT broker."
content_hash: 39a1ef759df3adcfbde11275d092406cd91d4110
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/mosquitto.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mosquitto

An MQTT broker.
More information: <https://mosquitto.org/>.

- Start Mosquitto:

`mosquitto`

- Specify a configuration file to use:

`mosquitto --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.conf</span>

- Listen on a specific port:

`mosquitto --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8883</span>

- Daemonize by forking into the background:

`mosquitto --daemon`
