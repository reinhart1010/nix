---
layout: page
title: common/install-tl (English)
description: "TeX Live cross-platform installer."
content_hash: a13e9b63e6029ce2bbd3836f887cfb2f63b2fbb6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# install-tl

TeX Live cross-platform installer.
More information: <https://tug.org/texlive/>.

- Start the text-based installer (default on Unix systems):

`install-tl -no-gui`

- Start the GUI installer (default on macOS and Windows, requires Tcl/Tk):

`install-tl -gui`

- Install TeX Live as defined in a specific profile file:

`install-tl -profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/texlive.profile</span>

- Start the installer with the settings from a specific profile file:

`install-tl -init-from-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/texlive.profile</span>

- Start the installer for installation on a portable device, like a USB stick:

`install-tl -portable`

- Show help for `install-tl`:

`install-tl -help`
