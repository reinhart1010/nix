---
layout: page
title: windows/takeown (English)
description: "Take ownership of a file or directory."
content_hash: 5269c37695c04ed0ead92aff44c7178d860a2b54
related_topics:
  - title: 中文 version
    url: /zh/windows/takeown.html
    icon: bi bi-globe
---
# takeown

Take ownership of a file or directory.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/takeown>.

- Take ownership of the specified file:

`takeown /f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Take ownership of the specified directory:

`takeown /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Take ownership of the specified directory and all subdirectories:

`takeown /r /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Change ownership to the Administrator group instead of the current user:

`takeown /a /f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
