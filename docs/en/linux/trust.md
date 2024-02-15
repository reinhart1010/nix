---
layout: page
title: linux/trust (English)
description: "Operate on the trust policy store."
content_hash: e4b2cf8e668d13c5b2115221b85a934b23038a82
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# trust

Operate on the trust policy store.
More information: <https://manned.org/trust>.

- List trust policy store items:

`trust list`

- List information about specific items in the trust policy store:

`trust list --filter=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blocklist|ca-anchors|certificates|trust-policy</span>

- Store a specific trust anchor in the trust policy store:

`trust anchor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/certificate.crt</span>

- Remove a specific anchor from the trust policy store:

`trust anchor --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/certificate.crt</span>

- Extract trust policy from the shared trust policy store:

`trust extract --format=x509-directory --filter=ca-anchors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display help for a subcommand:

`trust `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
