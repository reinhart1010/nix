---
layout: page
title: common/dmd (English)
description: "Official D compiler."
content_hash: 1d0d50e7765b9edb43e4e1a69ceed0bcad1e3d6c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dmd

Official D compiler.
More information: <https://dlang.org/dmd.html>.

- Build a D source file:

`dmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.d</span>

- Generate code for all template instantiations:

`dmd -allinst`

- Control bounds checking:

`dmd -boundscheck=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|safeonly|off</span>

- List information on all available checks:

`dmd -check=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">h|help|?</span>

- Turn on colored console output:

`dmd -color`
