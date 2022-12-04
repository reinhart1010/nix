---
layout: page
title: common/gnomon (English)
description: "Utility to annotate console logging statements with timestamps and find slow processes."
content_hash: bbbd5a89450ff3cb54d93ca60f7f75318291bc12
last_modified_at: 2022-12-04
---
# gnomon

Utility to annotate console logging statements with timestamps and find slow processes.
More information: <https://github.com/paypal/gnomon>.

- Use UNIX (or DOS) pipes to pipe the `stdout` of any command through gnomon:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon`

- Show number of seconds since the start of the process:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon --type=elapsed-total`

- Show an absolute timestamp in UTC:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon --type=absolute`

- Set a high threshold of 0.5 seconds for the elapsed time; exceeding which the timestamp will be colored bright red:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon --high `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>

- Set a medium threshold of 0.2 seconds (Timestamp will be colored bright yellow):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon --medium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.2</span>
