---
layout: page
title: common/rector (English)
description: "An automated tool for updating and refactoring PHP 5.3+ code."
content_hash: 610f93bf1a35a903c3d67728255d2262025756cc
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rector

An automated tool for updating and refactoring PHP 5.3+ code.
More information: <https://github.com/rectorphp/rector>.

- Process a specific directory:

`rector process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Process a directory without applying changes (dry run):

`rector process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --dry-run`

- Process a directory and apply coding standards:

`rector process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --with-style`

- Display a list of available levels:

`rector levels`

- Process a directory with a specific level:

`rector process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level_name</span>
