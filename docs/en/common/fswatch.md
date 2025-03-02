---
layout: page
title: common/fswatch (English)
description: "A cross-platform file change monitor."
content_hash: ed349743f72fb72915f47f14106a09b9b2e3b622
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/fswatch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fswatch

A cross-platform file change monitor.
More information: <https://emcrisostomo.github.io/fswatch>.

- Run a Bash command on file creation, update or deletion:

`fswatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | xargs -n 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash_command</span>

- Watch one or more files and/or directories:

`fswatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/another_directory/**/*.js</span>` | xargs -n 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash_command</span>

- Print the absolute paths of the changed files:

`fswatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` | xargs -n 1 -I {} echo {}`

- Filter by event type:

`fswatch --event `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Updated|Removed|Created|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` | xargs -n 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash_command</span>
