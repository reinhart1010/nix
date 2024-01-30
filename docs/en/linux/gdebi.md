---
layout: page
title: linux/gdebi (English)
description: "Simple tool to install `.deb` files."
content_hash: 4fd3d340b98ad451871e485efec07365dfc25f52
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# gdebi

Simple tool to install `.deb` files.
More information: <https://www.commandlinux.com/man-page/man1/gdebi.1.html>.

- Install local `.deb` packages resolving and installing its dependencies:

`gdebi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.deb</span>

- Do not show progress information:

`gdebi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.deb</span>` --quiet`

- Set an APT configuration option:

`gdebi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.deb</span>` --option=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">APT_OPTS</span>

- Use alternative root dir:

`gdebi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.deb</span>` --root=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/root_dir</span>

- Display version:

`gdebi --version`
