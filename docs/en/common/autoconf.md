---
layout: page
title: common/autoconf (English)
description: "Generate configuration scripts to automatically configure software source code packages."
content_hash: 5b21803ae766211e7bbd980094ff882bc36f9c95
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/autoconf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autoconf

Generate configuration scripts to automatically configure software source code packages.
More information: <https://www.gnu.org/software/autoconf>.

- Generate a configuration script from `configure.ac` (if present) or `configure.in` and save this script to `configure`:

`autoconf`

- Generate a configuration script from the specified template; output to `stdout`:

`autoconf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template-file</span>

- Generate a configuration script from the specified template (even if the input file has not changed) and write the output to a file:

`autoconf --force --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">outfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template-file</span>
