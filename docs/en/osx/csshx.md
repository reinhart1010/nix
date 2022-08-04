---
layout: page
title: osx/csshx (English)
description: "Cluster SSH tool for macOS."
content_hash: 2def0b0667db26f27e6f8d4263781abc8fd05049
---
# csshX

Cluster SSH tool for macOS.
More information: <https://github.com/brockgr/csshx>.

- Connect to multiple hosts:

`csshX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname2</span>

- Connect to multiple hosts with a given SSH key:

`csshX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@hostname1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@hostname2</span>` --ssh_args "-i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ssh_key.pem</span>`"`

- Connect to a pre-defined cluster from `/etc/clusters`:

`csshX cluster1`
