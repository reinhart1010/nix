---
layout: page
title: common/bear (English)
description: "A tool to generate compilation databases for `clang` tooling."
content_hash: d89c348e87f6c4178c27f4f3cb15c72c919f007b
last_modified_at: 2024-10-21
tldri18n_status: 2
---
# bear

A tool to generate compilation databases for `clang` tooling.
More information: <https://github.com/rizsotto/Bear>.

- Generate `compile_commands.json` by running a build command:

`bear -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- Generate compilation database with a custom output file name:

`bear --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compile_commands.json</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- Append results to an existing `compile_commands.json` file:

`bear --append -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- Run in verbose mode to get detailed output:

`bear --verbose -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- Force `bear` to use the preload method for command interception:

`bear --force-preload -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>
