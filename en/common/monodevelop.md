---
layout: page
title: common/monodevelop (English)
description: "Cross platform IDE for C#, F# and more."
content_hash: 41063c61376fcae366641cafa1dfbe26673d8bf6
---
# monodevelop

Cross platform IDE for C#, F# and more.
More information: <https://www.monodevelop.com/>.

- Start MonoDevelop:

`monodevelop`

- Open a specific file:

`monodevelop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a specific file with the caret at a specific position:

`monodevelop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`;`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>`;`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column_number</span>

- Force opening a new window instead of switching to an existing one:

`monodevelop --new-window`

- Disable redirection of stdout and stderr to a log file:

`monodevelop --no-redirect`

- Enable performance monitoring:

`monodevelop --perf-log`
