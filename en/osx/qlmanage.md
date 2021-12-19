---
layout: page
title: osx/qlmanage (English)
description: "QuickLook server tool."
content_hash: e6ac95f6d9e95c601a6f4fba5f85c449ead0d57b
related_topics:
  - title: 中文 version
    url: /zh/osx/qlmanage.html
    icon: bi bi-globe
---
# qlmanage

QuickLook server tool.

- Display QuickLook for one or multiple files:

`qlmanage -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename2</span>

- Compute 300px wide PNG thumbnails of all JPEGs in the current directory and put them in a directory:

`qlmanage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` -t -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Reset QuickLook:

`qlmanage -r`
