---
layout: page
title: common/readonly (English)
description: "Set read-only shell variables."
content_hash: 3e335f12bbf7122028fabbdfd41552da556c45c5
last_modified_at: 2024-01-08
tldri18n_status: 2
---
# readonly

Set read-only shell variables.
More information: <https://manned.org/readonly.1posix>.

- Set a read-only variable:

`readonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Mark a variable as read-only:

`readonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">existing_variable</span>

- [p]rint the names and values of all read-only variables to `stdout`:

`readonly -p`
