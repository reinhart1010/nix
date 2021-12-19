---
layout: page
title: common/rr (English)
description: "Debugging tool designed to record and replay program execution."
content_hash: b8ff5ea8877dcf88fd522cd101984b5383aa418d
---
# rr

Debugging tool designed to record and replay program execution.
More information: <https://rr-project.org/>.

- Record an application:

`rr record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary --arg1 --arg2</span>

- Replay latest recorded execution:

`rr replay`
