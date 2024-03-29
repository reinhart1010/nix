---
layout: page
title: common/f3write (English)
description: "Fill a drive out with .h2w files to test its real capacity."
content_hash: b3771cfdb6e5986821977839a64c50a1d56cc9a7
last_modified_at: 2023-11-23
tldri18n_status: 2
---
# f3write

Fill a drive out with .h2w files to test its real capacity.
See also: `f3read`, `f3probe`, `f3fix`.
More information: <http://oss.digirati.com.br/f3/>.

- Write test files to a given directory, filling the drive:

`f3write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Limit the write speed:

`f3write --max-write-rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kb_per_second</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>
