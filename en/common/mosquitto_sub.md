---
layout: page
title: common/mosquitto_sub (English)
description: "A simple MQTT version 3.1.1 client that will subscribe to topics and print the messages that it receives."
content_hash: b160a4b9b9d8c834c5e884764663b4455f5cbb2a
---
# mosquitto_sub

A simple MQTT version 3.1.1 client that will subscribe to topics and print the messages that it receives.
More information: <https://mosquitto.org/man/mosquitto_sub-1.html>.

- Subscribe to the topic `sensors/temperature` information with Quality of Service (`QoS`) set to 1. (The default hostname is `localhost` and port 1883):

`mosquitto_sub -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/temperature</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Subscribe to all broker status messages publishing on `iot.eclipse.org` port 1885 and print published messages verbosely:

`mosquitto_sub -v -h "iot.eclipse.org" -p 1885 -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\$SYS/#</span>

- Subscribe to multiple topics matching a given pattern. (+ takes any metric name):

`mosquitto_sub -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sensors/machines/+/temperature/+</span>
