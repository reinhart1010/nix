---
layout: page
title: linux/mumble (English)
description: "Low-latency, high quality voice chat software."
content_hash: b924bc72d824ea18c4067b5fb20277da34a84e9c
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mumble

Low-latency, high quality voice chat software.
More information: <https://www.mumble.info>.

- Open Mumble:

`mumble`

- Open Mumble and immediately connect to a server:

`mumble mumble://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open Mumble and immediately connect to a password protected server:

`mumble mumble://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Mute/unmute the microphone in a running Mumble instance:

`mumble rpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mute|unmute</span>

- Mute/unmute the microphone and the audio output of Mumble:

`mumble rpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deaf|undeaf</span>
