---
layout: page
title: common/lsyncd (English)
description: "Watch files and directories and run `rsync` when they change."
content_hash: ebd280017d608939418dd984036183bf23cb9fe4
last_modified_at: 2023-10-04
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lsyncd

Watch files and directories and run `rsync` when they change.
It is often used to keep two directories on separate systems in sync, ensuring that changes made in one directory are immediately mirrored to the other.
More information: <https://github.com/lsyncd/lsyncd>.

- Watch the source for changes and run `rsync` to synchronize files to the destination on every change:

`lsyncd -rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host::share_name</span>

- Use SSH instead of `rsyncd` shares:

`lsyncd -rsyncssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>
