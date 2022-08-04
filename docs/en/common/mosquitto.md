---
layout: page
title: common/mosquitto (English)
description: "An MQTT broker."
content_hash: 6fa1e40fff55baa39505ebfb4a257e38b991fd58
---
# mosquitto

An MQTT broker.
More information: <https://mosquitto.org/>.

- Start mosquitto:

`mosquitto`

- Specify a configuration file to use:

`mosquitto --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.conf</span>

- Listen on a specific port:

`mosquitto --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8883</span>

- Daemonize by forking into the background:

`mosquitto --daemon`
