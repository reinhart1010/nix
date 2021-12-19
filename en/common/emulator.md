---
layout: page
title: common/emulator (English)
description: "Manager Android emulators from the command-line."
content_hash: b7cceb657a8dd37dc9c118aa6f61bbb37d705f21
---
# emulator

Manager Android emulators from the command-line.
More information: <https://developer.android.com/studio/run/emulator-commandline>.

- Display the help:

`emulator -help`

- Start an Android emulator device:

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Display the webcams on your development computer that are available for emulation:

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` -webcam-list`

- Start an emulator overriding the facing back camera setting (use `-camera-front` for front camera):

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` -camera-back `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|emulated|webcamN</span>

- Start an emulator, with a maximum network speed:

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` -netspeed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gsm|hscsd|gprs|edge|hsdpa|lte|evdo|full</span>

- Start an emulator with network latency:

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` -netdelay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gsm|hscsd|gprs|edge|hsdpa|lte|evdo|none</span>

- Start an emulator, making all TCP connections through a specified HTTP/HTTPS proxy (port number is required):

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` -http-proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com:80</span>

- Start an emulator with a given SD card partition image file:

`emulator -avd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` -sdcard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/sdcard.img</span>
