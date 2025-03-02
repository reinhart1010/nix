---
layout: page
title: windows/es (English)
description: "Command-line interface for Everything, a fast file and folder search tool for Windows."
content_hash: a62f987abf762a6970835e586e800320b6f14e40
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/windows/es.html
    icon: bi bi-globe
tldri18n_status: 2
---
# es

Command-line interface for Everything, a fast file and folder search tool for Windows.
Requires Everything to be installed and running in the background.
More information: <https://www.voidtools.com/support/everything/command_line_interface/>.

- Search for a file or folder by name:

`es `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Search using a regular expression:

`es -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex_pattern</span>

- Match whole words:

`es -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Limit the number of results shown:

`es -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Search within a specific folder:

`es -path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">folder_path</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- List folders only:

`es /ad`

- List files only:

`es /a-d`

- Sort results (e.g., by name):

`es -sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name-ascending</span>
