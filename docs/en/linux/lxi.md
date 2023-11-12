---
layout: page
title: linux/lxi (English)
description: "Control LXI compatible instruments such as oscilloscopes."
content_hash: 71d9afb4019cc34a789d5edfac193949decc4231
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lxi

Control LXI compatible instruments such as oscilloscopes.
More information: <https://github.com/lxi-tools/lxi-tools>.

- Discover LXI devices on available networks:

`lxi discover`

- Capture a screenshot, detecting a plugin automatically:

`lxi screenshot --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>

- Capture a screenshot using a specified plugin:

`lxi screenshot --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` --plugin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rigol-1000z</span>

- Send an SCPI command to an instrument:

`lxi scpi --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*IDN?</span>`"`

- Run a benchmark for request and response performance:

`lxi benchmark --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>
