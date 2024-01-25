---
layout: page
title: windows/expand (English)
description: "Uncompress Windows Cabinet files."
content_hash: 9b315e7949684549f5c91b0ec27bed688d60ba10
last_modified_at: 2024-01-25
related_topics:
  - title: 中文 version
    url: /zh/windows/expand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# expand

Uncompress Windows Cabinet files.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/expand>.

- Uncompress a single-file Cabinet file to the specified directory:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Display the list of files in a source Cabinet file:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>` -d`

- Uncompress all files from the Cabinet file:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>` -f:*`

- Uncompress a specific file from a Cabinet file:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>` -f:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- Ignore the directory structure when uncompressing, and add them to a single directory:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>` -i`
