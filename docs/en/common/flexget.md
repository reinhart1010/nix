---
layout: page
title: common/flexget (English)
description: "A multipurpose automation tool for content like torrents, nzbs, podcasts, comics, series, movies, etc."
content_hash: 1b7d915d882960a998a18920a95b4678a1158522
last_modified_at: 2024-12-04
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/flexget.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># flexget

A multipurpose automation tool for content like torrents, nzbs, podcasts, comics, series, movies, etc.
More information: <https://flexget.com/en/CLI>.

- Run all Flexget tasks now:

`flexget execute --now`

- Start the Flexget daemon and daemonize its process:

`flexget daemon start --daemonize`

- List all series recorded in Flexget:

`flexget series list`

- Run a task from a config file:

`flexget -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.yml</span>` execute --task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>
