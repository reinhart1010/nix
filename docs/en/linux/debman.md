---
layout: page
title: linux/debman (English)
description: "Read man pages from uninstalled packages."
content_hash: 753e0dde430aad3e4b346330c0d93ddfdecf8740
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# debman

Read man pages from uninstalled packages.
More information: <https://manpages.debian.org/latest/debian-goodies/debman.1.html>.

- Read a man page for a command that is provided by a specified package:

`debman -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Specify a package version to download:

`debman -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Read a man page in a `.deb` file:

`debman -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
