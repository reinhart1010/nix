---
layout: page
title: common/ts (English)
description: "Add timestamps to every line from `stdin`."
content_hash: a1c476a55cba9614d791a725340156bc4cdf7789
last_modified_at: 2023-08-09
---
# ts

Add timestamps to every line from `stdin`.
More information: <https://joeyh.name/code/moreutils/>.

- Add a timestamp to the beginning of each line:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | ts`

- Add timestamps with microsecond precision:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | ts "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%b %d %H:%M:%.S</span>`"`

- Add [i]ncremental timestamps with microsecond precision, starting from zero:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | ts -i "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%H:%M:%.S</span>`"`

- Convert existing timestamps in a text file (eg. a log file) into [r]elative format:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | ts -r`
