---
layout: page
title: common/gitk (English)
description: "A graphical Git repository browser."
content_hash: 92a5621f1511ae15b6bef4cb700b211102b615cb
---
# gitk

A graphical Git repository browser.
More information: <https://git-scm.com/docs/gitk>.

- Show the repository browser for the current Git repository:

`gitk`

- Show repository browser for a specific file or directory:

`gitk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Show commits made since 1 week ago:

`gitk --since="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1 week ago</span>`"`

- Show commits older than 1/1/2016:

`gitk --until="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1/1/2015</span>`"`

- Show at most 100 changes in all branches:

` gitk --max-count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --all`
