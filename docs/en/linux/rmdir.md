---
layout: page
title: linux/rmdir (English)
description: "Remove directories without files."
content_hash: cfa157289587f8ccc207df0f2842c885fe2fc59a
last_modified_at: 2023-01-07
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rmdir

Remove directories without files.
See also: `rm`.
More information: <https://www.gnu.org/software/coreutils/rmdir>.

- Remove specific directories:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Remove specific nested directories recursively:

`rmdir --parents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>
