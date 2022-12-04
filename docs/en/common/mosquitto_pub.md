---
layout: page
title: common/mosquitto_pub (English)
description: "A simple MQTT version 3.1.1 client that will publish a single message on a topic and exit."
content_hash: 02801feb109ae1eabc40da0b00757144ab7bd991
last_modified_at: 2022-12-04
---
# mosquitto_pub

A simple MQTT version 3.1.1 client that will publish a single message on a topic and exit.
More information: <https://mosquitto.org/man/mosquitto_pub-1.html>.

- Publish a temperature value of 32 on the topic `sensors/temperature` to 192.168.1.1 (defaults to `localhost`) with Quality of Service (`QoS`) set to 1:

`mosquitto_pub -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/temperature</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">32</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Publish timestamp and temperature data on the topic `sensors/temperature` to a remote host on a non-standard port:

`mosquitto_pub -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1885</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/temperature</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1266193804 32</span>`"`

- Publish light switch status and retain the message on the topic `switches/kitchen_lights/status` to a remote host because there may be a long period of time between light switch events:

`mosquitto_pub -r -h "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iot.eclipse.org</span>`" -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">switches/kitchen_lights/status</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on</span>`"`

- Send the contents of a file (`data.txt`) as a message and publish it to `sensors/temperature` topic:

`mosquitto_pub -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/temperature</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.txt</span>

- Send the contents of a file (`data.txt`), by reading from `stdin` and send the entire input as a message and publish it to `sensors/temperature` topic:

`mosquitto_pub -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/temperature</span>` -s < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.txt</span>

- Read newline delimited data from `stdin` as a message and publish it to `sensors/temperature` topic:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo data.txt</span>` | mosquitto_pub -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/temperature</span>` -l`
