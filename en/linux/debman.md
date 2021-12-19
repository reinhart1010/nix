---
layout: page
title: linux/debman (English)
description: "Read man pages from uninstalled packages."
content_hash: 8020465503116aa55e58b09de0f71f3f8e2f792e
---
# debman

Read man pages from uninstalled packages.
More information: <https://manpages.debian.org/latest/debian-goodies/debman.1.html>.

- Read a man page for a command that is provided by a specified package name:

`debman -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>

- Specify a package version to download:

`debman -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>

- Read a man page in a `.deb` file:

`debman -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>
