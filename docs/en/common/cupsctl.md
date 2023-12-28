---
layout: page
title: common/cupsctl (English)
description: "Update or query a server's `cupsd.conf`."
content_hash: 7a925e76d2a710a93c7a70adb01e54ef9aa8c069
last_modified_at: 2023-12-28
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/cupsctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsctl

Update or query a server's `cupsd.conf`.
More information: <https://openprinting.github.io/cups/doc/man-cupsctl.html>.

- Display the current configuration values:

`cupsctl`

- Display the configuration values of a specific server:

`cupsctl -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server[:port]</span>

- Enable encryption on the connection to the scheduler:

`cupsctl -E`

- Enable or disable debug logging to the `error_log` file:

`cupsctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--debug-logging|--no-debug-logging</span>

- Enable or disable remote administration:

`cupsctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--remote-admin|--no-remote-admin</span>

- Parse the current debug logging state:

`cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'`
