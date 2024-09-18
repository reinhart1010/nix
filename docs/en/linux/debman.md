---
layout: page
title: linux/debman (English)
description: "Read man pages from uninstalled packages."
content_hash: 6cda8b39a03a084988d392e98b235f44a640333c
last_modified_at: 2024-09-18
tldri18n_status: 2
---
# debman

Read man pages from uninstalled packages.
More information: <https://manned.org/debman.1>.

- Read a man page for a command that is provided by a specified package:

`debman -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Specify a package version to download:

`debman -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Read a man page in a `.deb` file:

`debman -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
