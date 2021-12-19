---
layout: page
title: common/sops (English)
description: "SOPS: Secrets OPerationS."
content_hash: 9338abac15ed193ef5d2a6d3f5969c83525ccb13
---
# sops

SOPS: Secrets OPerationS.
Tool for managing secrets.
More information: <https://github.com/mozilla/sops>.

- Encrypt a file:

`sops -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/myfile.json</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/myfile.enc.json</span>

- Decrypt a file to the standard output:

`sops -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/myfile.enc.json</span>

- Rotate data keys for a sops file:

`sops -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/myfile.enc.yaml</span>

- Change the extension of the file once encrypted:

`sops -d --input-type json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/myfile.enc.json</span>

- Extract keys by naming them, and array elements by numbering them:

`sops -d --extract '["an_array"][1]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/myfile.enc.json</span>

- Show the difference between two sops files:

`diff <(sops -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret1.enc.yaml</span>`) <(sops -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/secret2.enc.yaml</span>`)`
