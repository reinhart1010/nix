---
layout: page
title: linux/ntpdate (English)
description: "Synchronize and set the date and time via NTP."
content_hash: a5ac08395a6bc0e5c39a0c562b5954cb40163fad
---
# ntpdate

Synchronize and set the date and time via NTP.
More information: <http://support.ntp.org/documentation>.

- Synchronize and set date and time:

`sudo ntpdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Query the host without setting the time:

`ntpdate -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Use an unprivileged port in case a firewall is blocking privileged ports:

`sudo ntpdate -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Force time to be stepped using `settimeofday` instead of `slewed`:

`sudo ntpdate -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
