---
layout: page
title: windows/assoc (English)
description: "Display or change associations between file extensions and file types."
content_hash: e1c3530eef7de187240fbbf311eece3c55cc8f70
related_topics:
  - title: 日本語 version
    url: /ja/windows/assoc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/assoc.html
    icon: bi bi-globe
---
# assoc

Display or change associations between file extensions and file types.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/assoc>.

- List all associations between file extensions and file types:

`assoc`

- Display the associated file type for a specific extension:

`assoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.txt</span>

- Set the associated file type for a specific extension:

`assoc .`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txtfile</span>
