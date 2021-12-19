---
layout: page
title: common/xephyr (English)
description: "A nested X server that runs as an X application."
content_hash: 260133a1c59ccf93f053cd4e9912c6f32672b9c8
---
# Xephyr

A nested X server that runs as an X application.
More information: <https://manned.org/xserver-xephyr>.

- Create a black window with display ID ":2":

`Xephyr -br -ac -noreset -screen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:2</span>

- Start an X application on the new screen:

`DISPLAY=:2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>
