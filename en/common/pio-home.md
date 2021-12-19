---
layout: page
title: common/pio-home (English)
description: "Launch the PlatformIO Home web server."
content_hash: 78a8718df2b603392452dd2f1890a902e8579745
---
# pio home

Launch the PlatformIO Home web server.
More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>.

- Open PlatformIO Home in the default web browser:

`pio home`

- Use a specific HTTP port (defaults to 8008):

`pio home --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Bind to a specific IP address (defaults to 127.0.0.1):

`pio home --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>

- Do not automatically open PlatformIO Home in the default web browser:

`pio home --no-open`

- Automatically shutdown the server on timeout (in seconds) when no clients are connected:

`pio home --shutdown-timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time</span>

- Specify a unique session identifier to keep PlatformIO Home isolated from other instances and protected from 3rd party access:

`pio home --session-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>
