---
layout: page
title: common/jmeter (English)
description: "Open source Java application designed for load testing functional behavior and measure performance."
content_hash: b16d9a230e324a121b4aedc16c71e76ec9dd1b55
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# jmeter

Open source Java application designed for load testing functional behavior and measure performance.
More information: <https://jmeter.apache.org>.

- Run a specific test plan in nongui mode:

`jmeter --nongui --testfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jmx</span>

- Run a test plan in nongui mode using a specific log file:

`jmeter --nogui --testfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jmx</span>` --logfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/logfile.jtl</span>

- Run a test plan in nongui mode using a specific proxy:

`jmeter --nongui --testfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jmx</span>` --proxyHost `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>` --proxyPort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8888</span>

- Run a test plan in nongui mode using a specific JMeter property:

`jmeter --jmeterproperty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>`='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`' --nongui --testfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jmx</span>
