---
layout: page
title: common/transmission-edit (English)
description: "Modify announce URLs from torrent files."
content_hash: 8e154d3add867045c630c1d650f56f0a94b0ac60
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# transmission-edit

Modify announce URLs from torrent files.
See also: `transmission`.
More information: <https://manned.org/transmission-edit>.

- Add or remove a URL from a torrent's announce list:

`transmission-edit --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.torrent</span>

- Update a tracker's passcode in a torrent file:

`transmission-edit --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old-passcode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new-passcode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.torrent</span>
