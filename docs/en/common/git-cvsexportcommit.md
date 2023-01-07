---
layout: page
title: common/git-cvsexportcommit (English)
description: "Export a single `Git` commit to a CVS checkout."
content_hash: 490987adbcb20d115af811a12caf72a1c23b2d86
last_modified_at: 2023-01-07
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git cvsexportcommit

Export a single `Git` commit to a CVS checkout.
More information: <https://git-scm.com/docs/git-cvsexportcommit>.

- Merge a specific patch into CVS:

`git cvsexportcommit -v -c -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_cvs_checkout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_sha1</span>
