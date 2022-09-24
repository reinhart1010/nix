---
layout: page
title: common/autoconf (English)
description: "Generate configuration scripts to automatically configure software source code packages."
content_hash: 61794f76d7f9a795c63063d2f8a9cd0ee9c41573
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># autoconf

Generate configuration scripts to automatically configure software source code packages.
More information: <https://www.gnu.org/software/autoconf>.

- Generate a configuration script from `configure.ac` (if present) or `configure.in` and save this script to `configure`:

`autoconf`

- Generate a configuration script from the specified template; output to stdout:

`autoconf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template-file</span>

- Generate a configuration script from the specified template (even if the input file has not changed) and write the output to a file:

`autoconf --force --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">outfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template-file</span>
