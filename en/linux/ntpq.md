---
layout: page
title: linux/ntpq (English)
description: "Query the Network Time Protocol (NTP) daemon."
content_hash: bc0a4f2e86c0f4f47f0ff292bcb3c544feeb05e9
---
# ntpq

Query the Network Time Protocol (NTP) daemon.
More information: <https://www.eecis.udel.edu/~mills/ntp/html/ntpq.html>.

- Start `ntpq` in interactive mode:

`ntpq --interactive`

- Print a list of NTP peers:

`ntpq --peers`

- Print a list of NTP peers without resolving hostnames from IP addresses:

`ntpq --numeric --peers`

- Use `ntpq` in debugging mode:

`ntpq --debug-level`

- Print NTP system variables values:

`ntpq --command=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rv</span>
