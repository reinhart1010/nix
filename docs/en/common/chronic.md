---
layout: page
title: common/chronic (English)
description: "Display `stdout` and `stderr` of a command if and only if it fails."
content_hash: 098ce883a5bf8f21c85d12cd53ba945a70f41528
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# chronic

Display `stdout` and `stderr` of a command if and only if it fails.
More information: <https://joeyh.name/code/moreutils/>.

- Display `stdout` and `stderr` of the specified command if and only if it produces a non-zero exit code or crashes:

`chronic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command options ...</span>

- Display `stdout` and `stderr` of the specified command if and only if it produces a non-empty `stderr`:

`chronic -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command options ...</span>

- Enable [v]erbose mode:

`chronic -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command options ...</span>
