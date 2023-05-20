---
layout: page
title: common/ts (English)
description: "Add timestamps to every line from standard input."
content_hash: 899bd25914cc486164fa471c7394a3ce20b7c49a
last_modified_at: 2023-05-20
---
# ts

Add timestamps to every line from standard input.
More information: <https://joeyh.name/code/moreutils/>.

- Add a timestamp to the beginning of each line:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | ts`

- Add timestamps with microsecond precision:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | ts "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%b %d %H:%M:%.S</span>`"`

- Add [i]ncremental timestamps with microsecond precision, starting from zero:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | ts -i "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%H:%M:%.S</span>`"`

- Convert existing timestamps in a text file (eg. a log file) into [r]elative format:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | ts -r`
