---
layout: page
title: common/gnmic-subscribe (English)
description: "Subscribe to a gnmic network device state updates."
content_hash: fdf1285a02a18aa8e4af0c525850557299cad683
---
# gnmic subscribe

Subscribe to a gnmic network device state updates.
More information: <https://gnmic.kmrd.dev/cmd/subscribe>.

- Subscribe to target state updates under the subtree of a specific path:

`gnmic --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>

- Subscribe to a target with a sample interval of 30s (default is 10s):

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>` --sample-interval 30s`

- Subscribe to a target with sample interval and updates only on change:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>` --stream-mode on-change --heartbeat-interval 1m`

- Subscribe to a target for only one update:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>` --mode once`

- Subscribe to a target and specify response encoding (json_ietf):

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>` --encoding json_ietf`
