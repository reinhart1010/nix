---
layout: page
title: common/cupsctl (English)
description: "Update or query a server's `cupsd.conf`."
content_hash: bfb578fa70992e7db76b55170d98f7cfaf1f8bb0
last_modified_at: 2023-12-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsctl

Update or query a server's `cupsd.conf`.
More information: <https://www.cups.org/doc/man-cupsctl.html>.

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
