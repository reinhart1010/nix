---
layout: page
title: common/gh-release (English)
description: "Manage GitHub releases from the command-line."
content_hash: 609ef5af40b5763e6ed047785cc8f08be9bec7d1
---
# gh release

Manage GitHub releases from the command-line.
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

`gh release upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>
