---
layout: page
title: common/iperf3 (English)
description: "Traffic generator for testing network bandwidth."
content_hash: 0b4c0a3a98dbcc59f4cc6bdeaca8965661d174fa
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/iperf3.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iperf3

Traffic generator for testing network bandwidth.
More information: <https://iperf.fr>.

- Run iperf3 as a server:

`iperf3 -s`

- Run an iperf3 server on a specific port:

`iperf3 -s -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Start bandwidth test:

`iperf3 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>

- Run iperf3 in multiple parallel streams:

`iperf3 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">streams</span>

- Reverse direction of the test. Server sends data to the client:

`iperf3 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` -R`
