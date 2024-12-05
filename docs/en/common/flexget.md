---
layout: page
title: common/flexget (English)
description: "A multipurpose automation tool for content like torrents, nzbs, podcasts, comics, series, movies, etc."
content_hash: 1b7d915d882960a998a18920a95b4678a1158522
last_modified_at: 2024-12-05
tldri18n_status: 2
---
# flexget

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
