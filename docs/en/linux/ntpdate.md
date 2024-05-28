---
layout: page
title: linux/ntpdate (English)
description: "Synchronize and set the date and time via NTP."
content_hash: 6bf9d430ed224b6b34d8e3ac6acc9f7ee2919e24
last_modified_at: 2024-05-28
tldri18n_status: 2
---
# ntpdate

Synchronize and set the date and time via NTP.
More information: <https://manned.org/ntpdate>.

- Synchronize and set date and time:

`sudo ntpdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Query the host without setting the time:

`ntpdate -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Use an unprivileged port in case a firewall is blocking privileged ports:

`sudo ntpdate -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Force time to be stepped using `settimeofday` instead of `slewed`:

`sudo ntpdate -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
