---
layout: page
title: common/glab-release (English)
description: "Manage GitLab releases."
content_hash: 2ca102c06e92fb0bf4cd3533d5d2385d51bc39ed
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# glab release

Manage GitLab releases.
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

`glab release upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
