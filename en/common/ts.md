---
layout: page
title: common/ts (English)
description: "Add timestamps to every line from standard input."
content_hash: 7231885b70d4dca4c2a2117f9eead7dda19b1882
---
# ts

Add timestamps to every line from standard input.
More information: <https://joeyh.name/code/moreutils/>.

- Add a timestamp to the beginning of each line:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_command</span>` | ts`

- Add timestamps with microsecond precision:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_command</span>` | ts "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%b %d %H:%M:%.S</span>`"`

- Add [i]ncremental timestamps with microsecond precision, starting from zero:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_command</span>` | ts -i "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%H:%M:%.S</span>`"`

- Convert existing timestamps in a text file (eg. a log file) into [r]elative format:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | ts -r`
