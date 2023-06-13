---
layout: page
title: linux/tc (English)
description: "Show/manipulate traffic control settings."
content_hash: c1098fcd13f356d4b3bafe05017b13462d368fa3
last_modified_at: 2023-06-13
---
# tc

Show/manipulate traffic control settings.
More information: <https://manned.org/tc>.

- Add constant network delay to outbound packages:

`tc qdisc add dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` root netem delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delay_in_milliseconds</span>`ms`

- Add normal distributed network delay to outbound packages:

`tc qdisc add dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` root netem delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mean_delay_ms</span>`ms `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delay_std_ms</span>`ms`

- Add package corruption/loss/duplication to a portion of packages:

`tc qdisc add dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` root netem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">corruption|loss|duplication</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">effect_percentage</span>`%`

- Limit bandwidth, burst rate and max latency:

`tc qdisc add dev eth0 root tbf rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max_bandwidth_mb</span>`mbit burst `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max_burst_rate_kb</span>`kbit latency `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max_latency_before_drop_ms</span>`ms`

- Show active traffic control policies:

`tc qdisc show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Delete all traffic control rules:

`tc qdisc del dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Change traffic control rule:

`tc qdisc change dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` root netem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">policy</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">policy_parameters</span>
