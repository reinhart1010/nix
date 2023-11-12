---
layout: page
title: common/promtool (English)
description: "Tooling for the Prometheus monitoring system."
content_hash: 639922cf9deb7c559acdbbeae4e2ffc5ac6d4f7c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# promtool

Tooling for the Prometheus monitoring system.
More information: <https://prometheus.io/docs/prometheus/latest/getting_started/>.

- Check if the config files are valid or not (if present report errors):

`promtool check config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config_file.yml</span>

- Check if the rule files are valid or not (if present report errors):

`promtool check rules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rules_file.yml</span>

- Pass Prometheus metrics over `stdin` to check them for consistency and correctness:

`curl --silent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com:9090/metrics/</span>` | promtool check metrics`

- Unit tests for rules config:

`promtool test rules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test_file.yml</span>
