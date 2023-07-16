---
layout: page
title: common/gh-release (English)
description: "Manage GitHub releases."
content_hash: e6753d4fba88b31ef93df8d8ed18f31fe0026283
last_modified_at: 2023-07-16
---
# gh release

Manage GitHub releases.
More information: <https://cli.github.com/manual/gh_release>.

- List releases in a GitHub repository, limited to 30 items:

`gh release list`

- Display information about a specific release:

`gh release view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Create a new release:

`gh release create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Delete a specific release:

`gh release delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Download assets from a specific release:

`gh release download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Upload assets to a specific release:

`gh release upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
