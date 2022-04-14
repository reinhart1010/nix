---
layout: page
title: linux/faillock (English)
description: "Display and modify authentication failure record files."
content_hash: b78357e59470092c0e28b504747b9a370d32613e
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># faillock

Display and modify authentication failure record files.
More information: <https://manned.org/faillock>.

- List login failures of all users:

`sudo faillock`

- List login failures of the specified user:

`sudo faillock --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- Reset the failure records of the specified user:

`sudo faillock --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --reset`
