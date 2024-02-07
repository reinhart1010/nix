---
layout: page
title: common/bru (English)
description: "CLI for Bruno, an Opensource IDE for exploring and testing APIs."
content_hash: 4ef2a94703d0d81e8cef19b3c1d251d949120b7c
last_modified_at: 2024-02-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bru.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bru

CLI for Bruno, an Opensource IDE for exploring and testing APIs.
More information: <https://docs.usebruno.com/cli/overview.html>.

- Run all request files from the current directory:

`bru run`

- Run a single request from the current directory by specifying its filename:

`bru run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.bru</span>

- Run requests using an environment:

`bru run --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>

- Run requests using an environment with a variable:

`bru run --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>` --env-var `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_value</span>

- Run request and collect the results in an output file:

`bru run --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.json</span>

- Display help:

`bru run --help`
