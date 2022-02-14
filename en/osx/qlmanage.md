---
layout: page
title: osx/qlmanage (English)
description: "QuickLook server tool."
content_hash: d03255ee95e70ad2e535bd31e3a34900f07b9169
related_topics:
  - title: 中文 version
    url: /zh/osx/qlmanage.html
    icon: bi bi-globe
---
# qlmanage

QuickLook server tool.
More information: <https://ss64.com/osx/qlmanage.html>.

- Display QuickLook for one or multiple files:

`qlmanage -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename2</span>

- Compute 300px wide PNG thumbnails of all JPEGs in the current directory and put them in a directory:

`qlmanage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` -t -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Reset QuickLook:

`qlmanage -r`
