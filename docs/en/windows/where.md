---
layout: page
title: windows/where (English)
description: "Display the location of files that match the search pattern."
content_hash: 468b9a651f574f64aa5c9ac136721e1a54679d65
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/where.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/windows/where.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/where.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/where.html
    icon: bi bi-globe
tldri18n_status: 2
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

`where /R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>

- Silently return the error code for the location of the file pattern:

`where /Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>
