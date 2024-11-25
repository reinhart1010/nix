---
layout: page
title: linux/flatpak-mask (English)
description: "Mask out updates and automatic installation."
content_hash: b3efca56723cd15d0632a65cb0ee1a0fc5d8a372
last_modified_at: 2024-11-25
tldri18n_status: 2
---
# flatpak mask

Mask out updates and automatic installation.
More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-mask>.

- Ignore updates for a specific flatpak:

`flatpak mask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Undo ignore updates:

`flatpak mask --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- List all currently masked patterns:

`flatpak mask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--system|--user</span>
