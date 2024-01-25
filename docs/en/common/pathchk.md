---
layout: page
title: common/pathchk (English)
description: "Check the validity and portability of pathnames."
content_hash: 7a7408d56921ddfb1806d49f99c8d0a12f0ed0dc
last_modified_at: 2024-01-25
related_topics:
  - title: polski version
    url: /pl/common/pathchk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pathchk

Check the validity and portability of pathnames.
More information: <https://www.gnu.org/software/coreutils/pathchk>.

- Check pathnames for validity in the current system:

`pathchk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path1 path2 …</span>

- Check pathnames for validity on a wider range of POSIX compliant systems:

`pathchk -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path1 path2 …</span>

- Check pathnames for validity on all POSIX compliant systems:

`pathchk --portability `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path1 path2 …</span>

- Only check for empty pathnames or leading dashes (-):

`pathchk -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path1 path2 …</span>
