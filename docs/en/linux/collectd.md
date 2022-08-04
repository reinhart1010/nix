---
layout: page
title: linux/collectd (English)
description: "System statistics collection daemon."
content_hash: f98e4616d677a56cdd9754ffe152e9df919e7df2
---
# collectd

System statistics collection daemon.
More information: <https://collectd.org/>.

- Show usage help, including the program version:

`collectd -h`

- Test the configuration file and then exit:

`collectd -t`

- Test plugin data collection functionality and then exit:

`collectd -T`

- Start collectd:

`collectd`

- Specify a custom configuration file location:

`collectd -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Specify a custom PID file location:

`collectd -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Don't fork into the background:

`collectd -f`
