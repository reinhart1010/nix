---
layout: page
title: common/watchexec (English)
description: "Run arbitrary commands when files change."
content_hash: 68ec34d5cb9f76ef1a91d96fd36949afe07f96ed
---
# watchexec

Run arbitrary commands when files change.
More information: <https://github.com/watchexec/watchexec>.

- Call `ls -la` when any file in the current directory changes:

`watchexec -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -la</span>

- Run `make` when any JavaScript, CSS and HTML files in the current directory change:

`watchexec --exts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">js,css,html</span>` make`

- Run `make` when any file in the `lib` or `src` subdirectories change:

`watchexec --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lib</span>` --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">src</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- Call/restart `my_server` when any file in the current directory change, sending `SIGKILL` to stop the child process:

`watchexec --restart --signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGKILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_server</span>
