---
layout: page
title: common/influx (English)
description: "InfluxDB command-line client."
content_hash: 58c799f93d1bea39aa002737d3ad96d245a17e19
---
# influx

InfluxDB command-line client.
More information: <https://docs.influxdata.com/influxdb/v1.7/tools/shell/>.

- Connect to an InfluxDB running on localhost with no credentials:

`influx`

- Connect with a specific username (will prompt for a password):

`influx -username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -password ""`

- Connect to a specific host:

`influx -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Use a specific database:

`influx -database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>

- Execute a given command:

`influx -execute "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">influxql_command</span>`"`

- Return output in a specific format:

`influx -execute "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">influxql_command</span>`" -format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|csv|column</span>
