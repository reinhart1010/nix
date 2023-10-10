---
layout: page
title: common/open.fish (English)
description: "Opens files, directories, and URIs with default applications."
content_hash: 8c2928ccd0d52b27c33ad9fc949bf9c0ca6ee814
last_modified_at: 2023-10-10
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># open

Opens files, directories, and URIs with default applications.
This command is available through `fish` on operating systems without the built-in `open` command (e.g. Haiku and macOS).
More information: <https://fishshell.com/docs/current/cmds/open.html>.

- Open a file with the associated application:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ext</span>

- Open all the files of a given extension in the current directory with the associated application:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>

- Open a directory using the default file manager:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Open a website using the default web browser:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Open a specific URI using the default application that can handle it:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>
