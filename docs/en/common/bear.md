---
layout: page
title: common/bear (English)
description: "A tool to generate compilation databases for `clang` tooling."
content_hash: d89c348e87f6c4178c27f4f3cb15c72c919f007b
last_modified_at: 2024-10-20
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bear.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bear

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
