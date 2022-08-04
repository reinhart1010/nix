---
layout: page
title: common/glab-release (English)
description: "Manage GitLab releases from the command-line."
content_hash: e0242e9f036ffa1d1887c1c2bf6b4c75a77e9588
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># glab release

Manage GitLab releases from the command-line.
More information: <https://glab.readthedocs.io/en/latest/release>.

- List releases in a Gitlab repository, limited to 30 items:

`glab release list`

- Display information about a specific release:

`glab release view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Create a new release:

`glab release create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Delete a specific release:

`glab release delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Download assets from a specific release:

`glab release download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Upload assets to a specific release:

`glab release upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>
