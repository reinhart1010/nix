---
layout: page
title: common/cpan (English)
description: "Query, download and build perl modules from CPAN sites."
content_hash: 77f2883431a7eb1e72d8ab98873040c0f6689187
last_modified_at: 2024-10-19
tldri18n_status: 2
---
# cpan

Query, download and build perl modules from CPAN sites.
More information: <https://manned.org/cpan>.

- Install a module (`-i` is optional):

`cpan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Force install a module (`-i` is not optional):

`cpan -fi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Upgrade all installed modules:

`cpan -u`

- Recompile modules:

`cpan -r`
