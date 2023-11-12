---
layout: page
title: common/psgrep (English)
description: "Search running processes with `grep`."
content_hash: f2aab71b56b31cb0b0f9ece42bc2ea7c6bde6c23
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# psgrep

Search running processes with `grep`.
More information: <https://jvz.github.io/psgrep>.

- Find process lines containing a specific string:

`psgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- Find process lines containing a specific string, excluding headers:

`psgrep -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- Search using a simplified format (PID, user, command):

`psgrep -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>
