---
layout: page
title: common/czkawka-cli (English)
description: "Command-line version of `czkawka` a multi-functional app to find duplicates, empty folders, similar images and much more."
content_hash: 84c07ed5281c5d4fa5771b6b1542141f4ddbf908
last_modified_at: 2022-12-26
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># czkawka-cli

Command-line version of `czkawka` a multi-functional app to find duplicates, empty folders, similar images and much more.
More information: <https://github.com/qarmin/czkawka>.

- List duplicate or similar files in specific directories:

`czkawka-cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dup|image</span>` --directories `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Find duplicate files in specific directories and delete them (default: `NONE`):

`czkawka-cli dup --directories `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>` --delete-method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AEN|AEO|ON|OO|HARD|NONE</span>
