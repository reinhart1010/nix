---
layout: page
title: linux/nmon (English)
description: "A system administrator, tuner, and benchmark tool."
content_hash: e5fbb69d8371fe3d5659878ee39e3fe66dde764c
---
# nmon

A system administrator, tuner, and benchmark tool.

- Start nmon:

`nmon`

- Save records to file ("-s 300 -c 288" by default):

`nmon -f`

- Save records to file with a total of 240 measurements, by taking 30 seconds between each measurement:

`nmon -f -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">240</span>
