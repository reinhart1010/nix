---
layout: page
title: linux/hyprpm (English)
description: "Control plugins for the Hyprland Wayland compositor."
content_hash: 01006b96ac1fcb8e9b8298ae64a01a4649523bf4
last_modified_at: 2024-06-18
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/hyprpm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hyprpm

Control plugins for the Hyprland Wayland compositor.
More information: <https://wiki.hyprland.org/Plugins/Using-Plugins/#hyprpm>.

- Add a plugin:

`hyprpm add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_url</span>

- Remove a plugin:

`hyprpm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_url|plugin_name</span>

- Enable a plugin:

`hyprpm enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>

- Disable a plugin:

`hyprpm disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>

- Update and check all plugins:

`hyprpm update`

- Force an operation:

`hyprpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">operation</span>

- List all installed plugins:

`hyprpm list`
