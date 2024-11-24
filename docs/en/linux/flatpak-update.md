---
layout: page
title: linux/flatpak-update (English)
description: "Update flatpak applications and runtimes."
content_hash: 2f079e8e6265f5edf97255f9a82a7c5b8f4e8993
last_modified_at: 2024-11-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/flatpak-update.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># flatpak update

Update flatpak applications and runtimes.
More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-update>.

- Update all installed applications and runtimes (use `-y` to confirm all prompts automatically):

`flatpak update`

- Update only a specific app:

`flatpak update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Update/Downgrade to a specific commit (also see flatpak remote-info and flatpak mask):

`flatpak update --commit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">COMMIT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>
