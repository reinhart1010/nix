---
layout: page
title: windows/where (English)
description: "Display the location of files that match the search pattern."
content_hash: 80f66ee2de36fff13dbf58bd43baf13ebc4e8198
related_topics:
  - title: 中文 version
    url: /zh/windows/where.html
    icon: bi bi-globe
---
# where

Display the location of files that match the search pattern.
Defaults to current work directory and paths in the PATH environment variable.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/where>.

- Display the location of file pattern:

`where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>

- Display the location of file pattern including file size and date:

`where /T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>

- Recursively search for file pattern at specified path:

`where /R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>

- Silently return the error code for the location of the file pattern:

`where /Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>
