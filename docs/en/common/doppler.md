---
layout: page
title: common/doppler (English)
description: "Manage environment variables across different environments using Doppler."
content_hash: d28f7c2125111221ecae0eef229e1ff567a43269
last_modified_at: 2024-08-03
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doppler.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doppler

Manage environment variables across different environments using Doppler.
Some subcommands such as `doppler run` and `doppler secrets` have their own usage documentation.
More information: <https://docs.doppler.com/docs/cli>.

- Setup Doppler CLI in the current directory:

`doppler setup`

- Setup Doppler project and config in current directory:

`doppler setup`

- Run a command with secrets injected into the environment:

`doppler run --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- View your project list:

`doppler projects`

- View your secrets for current project:

`doppler secrets`

- Open doppler dashboard in browser:

`doppler open`
