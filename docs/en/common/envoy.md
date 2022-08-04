---
layout: page
title: common/envoy (English)
description: "A PHP-based task manager for Laravel remote servers."
content_hash: 8b8a402c156fd9cf10d6d7967c14baeb8dda568c
---
# envoy

A PHP-based task manager for Laravel remote servers.
More information: <https://laravel.com/docs/envoy>.

- Initialize a configuration file:

`envoy init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_name</span>

- Run a task:

`envoy run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>

- Run a task from a specific project:

`envoy run --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>

- Run a task and continue on failure:

`envoy run --continue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>

- Dump a task as a Bash script for inspection:

`envoy run --pretend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>

- Connect to the specified server via SSH:

`envoy ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_name</span>
