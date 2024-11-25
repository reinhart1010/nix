---
layout: page
title: linux/flatpak-update (English)
description: "Update flatpak applications and runtimes."
content_hash: 2f079e8e6265f5edf97255f9a82a7c5b8f4e8993
last_modified_at: 2024-11-25
tldri18n_status: 2
---
# flatpak update

Update flatpak applications and runtimes.
More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-update>.

- Update all installed applications and runtimes (use `-y` to confirm all prompts automatically):

`flatpak update`

- Update only a specific app:

`flatpak update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Update/Downgrade to a specific commit (also see flatpak remote-info and flatpak mask):

`flatpak update --commit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">COMMIT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>
