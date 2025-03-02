---
layout: page
title: common/pathchk (English)
description: "Check the validity and portability of pathnames."
content_hash: 3f96e3f0216c87c7c78cafd2384723a9a10f3e47
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/pathchk.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pathchk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/pathchk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pathchk

Check the validity and portability of pathnames.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/pathchk-invocation.html>.

- Check pathnames for validity in the current system:

`pathchk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path1 path2 …</span>

- Check pathnames for validity on a wider range of POSIX compliant systems:

`pathchk -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path1 path2 …</span>

- Check pathnames for validity on all POSIX compliant systems:

`pathchk --portability `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path1 path2 …</span>

- Only check for empty pathnames or leading dashes (-):

`pathchk -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path1 path2 …</span>
