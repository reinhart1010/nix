---
layout: page
title: common/emulator (English)
description: "Manage Android emulators."
content_hash: 3b17fe68f592e0c4cdfa067d662e9e5fb6542654
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# emulator

Manage Android emulators.
More information: <https://developer.android.com/studio/run/emulator-commandline>.

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

- Display help:

`emulator -help`
