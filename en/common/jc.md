---
layout: page
title: common/jc (English)
description: "A utility to convert the output of multiple commands to JSON."
content_hash: fd1f89f9d7e67ce68d15d371168780cd73d5d06e
---
# jc

A utility to convert the output of multiple commands to JSON.
More information: <https://github.com/kellyjonbrazil/jc>.

- Convert command output to JSON via pipe:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>` | jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--ifconfig</span>

- Convert command output to JSON via magic syntax:

`jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>

- Output pretty JSON via pipe:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>` | jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--ifconfig</span>` -p`

- Output pretty JSON via magic syntax:

`jc -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>
