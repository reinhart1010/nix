---
layout: page
title: linux/flatpak-remote-info (English)
description: "Show information about an application or runtime in a remote."
content_hash: cd5680104525198b07e95a3ec995d505b6c7cc74
last_modified_at: 2024-11-25
tldri18n_status: 2
---
# flatpak remote-info

Show information about an application or runtime in a remote.
More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remote-info>.

- Show information about a flatpak:

`flatpak remote-info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Show a log of previous versions in a remote:

`flatpak remote-info --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Show information about the specific commit, rather than the latest version:

`flatpak remote-info --commit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">COMMIT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>
