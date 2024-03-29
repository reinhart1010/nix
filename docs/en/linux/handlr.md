---
layout: page
title: linux/handlr (English)
description: "Manage your default applications."
content_hash: a33e13db66c3789873ccbf59b7223a63b828e9ea
last_modified_at: 2024-02-09
tldri18n_status: 2
---
# handlr

Manage your default applications.
More information: <https://github.com/chmln/handlr>.

- Open a URL in the default application:

`handlr open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Open a PDF in the default PDF viewer:

`handlr open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>

- Set `imv` as the default application for PNG files:

`handlr set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imv.desktop</span>

- Set MPV as the default application for all audio files:

`handlr set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'audio/*'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv.desktop</span>

- List all default apps:

`handlr list`

- Print the default application for PNG files:

`handlr get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.png</span>
