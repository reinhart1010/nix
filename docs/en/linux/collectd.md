---
layout: page
title: linux/collectd (English)
description: "System statistics collection daemon."
content_hash: d4c1ea608c163816e605fb3dd429e14cbc41c2b4
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# collectd

System statistics collection daemon.
More information: <https://collectd.org/>.

- Test the configuration file and then exit:

`collectd -t`

- Test plugin data collection functionality and then exit:

`collectd -T`

- Start `collectd`:

`collectd`

- Specify a custom configuration file location:

`collectd -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Specify a custom PID file location:

`collectd -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Don't fork into the background:

`collectd -f`

- Display help and version:

`collectd -h`
