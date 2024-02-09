---
layout: page
title: common/gnomon (English)
description: "Utility to annotate console logging statements with timestamps and find slow processes."
content_hash: 93e4fd7e0dcca19c0f3c83a79464acf2fd982e8c
last_modified_at: 2024-02-09
tldri18n_status: 2
---
# gnomon

Utility to annotate console logging statements with timestamps and find slow processes.
More information: <https://github.com/paypal/gnomon>.

- Use UNIX (or DOS) pipes to pipe `stdout` of any command through gnomon:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon`

- Show number of seconds since the start of the process:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon --type=elapsed-total`

- Show an absolute timestamp in UTC:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon --type=absolute`

- Use a high threshold of 0.5 seconds, exceeding which the timestamp will be colored bright red:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon --high 0.5`

- Use a medium threshold of 0.2 seconds, exceeding which the timestamp will be colored bright yellow:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon --medium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.2</span>
