---
layout: page
title: windows/assoc (English)
description: "Display or change associations between file extensions and file types."
content_hash: f4ecc63d0facde8f65d6cfa8f2c9c766b5145b80
last_modified_at: 2022-12-20
related_topics:
  - title: 日本語 version
    url: /ja/windows/assoc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/assoc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/assoc.html
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

- View the output of `assoc` one screen at a time:

`assoc | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">more</span>
