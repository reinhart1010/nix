---
layout: page
title: common/jc (English)
description: "Convert the output of multiple commands to JSON."
content_hash: faa18d10d2940fb01e78eb0555d727da0f8b0016
last_modified_at: 2024-04-26
tldri18n_status: 2
---
# jc

Convert the output of multiple commands to JSON.
More information: <https://github.com/kellyjonbrazil/jc>.

- Convert command output to JSON via pipe:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>` | jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--ifconfig</span>

- Convert command output to JSON via magic syntax:

`jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>

- Output pretty JSON via pipe:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>` | jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--ifconfig</span>` -p`

- Output pretty JSON via magic syntax:

`jc -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>
