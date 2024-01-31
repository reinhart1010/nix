---
layout: page
title: osx/qlmanage (English)
description: "QuickLook server tool."
content_hash: d165239bd58767586dbb6ecd5974a2b17ac489ab
last_modified_at: 2024-01-31
related_topics:
  - title: 中文 version
    url: /zh/osx/qlmanage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qlmanage

QuickLook server tool.
More information: <https://keith.github.io/xcode-man-pages/qlmanage.1.html>.

- Display QuickLook for one or multiple files:

`qlmanage -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Compute 300px wide PNG thumbnails of all JPEGs in the current directory and put them in a directory:

`qlmanage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` -t -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Reset QuickLook:

`qlmanage -r`
