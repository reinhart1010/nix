---
layout: page
title: common/stressapptest (English)
description: "Userspace memory and IO test."
content_hash: b0a5f57d0961d481c085d6644b8683718eda12fe
last_modified_at: 2023-09-05
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># stressapptest

Userspace memory and IO test.
More information: <https://github.com/stressapptest/stressapptest>.

- Test the given amount of memory (in Megabytes):

`stressapptest -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">memory</span>

- Test memory as well as I/O for the given file:

`stressapptest -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">memory</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Test specifying the verbosity level, where 0=lowest, 20=highest, 8=default:

`stressapptest -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">memory</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>
