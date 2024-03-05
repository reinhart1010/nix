---
layout: page
title: common/pamsplit (English)
description: "Split a multi-image Netpbm file into multiple single-image Netpbm files."
content_hash: 615b89d2130f9f26dc8fc5611f893dba7677f90a
last_modified_at: 2024-03-05
tldri18n_status: 2
---
# pamsplit

Split a multi-image Netpbm file into multiple single-image Netpbm files.
See also: `pamfile`, `pampick`, `pamexec`.
More information: <https://netpbm.sourceforge.net/doc/pamsplit.html>.

- Split a multi-image Netpbm file into multiple single-image Netpbm files:

`pamsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>

- Specify a pattern for naming output files:

`pamsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_%d.pam</span>
