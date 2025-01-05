---
layout: page
title: linux/scriptlive (English)
description: "Execute a typescript created by the `script` command in real-time."
content_hash: f145b4953a7303c4450843288b36c0d100acace7
last_modified_at: 2025-01-05
tldri18n_status: 2
---
# scriptlive

Execute a typescript created by the `script` command in real-time.
See also: `script`.
More information: <https://manned.org/scriptlive>.

- Execute a typescript in real-time:

`scriptlive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/timing_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/typescript</span>

- Execute a typescript at double the original speed:

`scriptlive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/timing_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/typescript</span>` --divisor 2`

- Execute a typescript created using `--log-in` option of `script`:

`scriptlive --log-in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/stdin_log_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/typescript</span>

- Execute a typescript waiting at most 2 seconds between each command:

`scriptlive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/timing_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/typescript</span>` --maxdelay 2`
