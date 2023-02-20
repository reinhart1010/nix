---
layout: page
title: osx/csshx (English)
description: "Cluster SSH tool for macOS."
content_hash: 0299a80cd0bf44c8e9fde9999ed01c8868db6f4c
last_modified_at: 2023-02-20
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/csshx.html
    icon: bi bi-globe
---
# csshX

Cluster SSH tool for macOS.
More information: <https://github.com/brockgr/csshx>.

- Connect to multiple hosts:

`csshX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname2</span>

- Connect to multiple hosts with a given SSH key:

`csshX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@hostname1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@hostname2</span>` --ssh_args "-i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key_file.pem</span>`"`

- Connect to a pre-defined cluster from `/etc/clusters`:

`csshX cluster1`
