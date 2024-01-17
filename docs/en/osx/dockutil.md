---
layout: page
title: osx/dockutil (English)
description: "Manage macOS dock items."
content_hash: 04b7fe3d86234c1aca10873c52e4cd2b487887cf
last_modified_at: 2024-01-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/dockutil.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dockutil

Manage macOS dock items.
More information: <https://github.com/kcrawford/dockutil>.

- Add an application to the end of the current user's dock:

`dockutil --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/application</span>

- Replace one application with another in the current user's dock:

`dockutil --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/application</span>` --replacing '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dock_item_label</span>`'`

- Add a directory with view options and display it as a folder icon or stack:

`dockutil --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/directory</span>` --view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grid|fan|list|auto</span>` --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">folder|stack</span>

- Add a URL dock item after another item:

`dockutil --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vnc://example_server.local</span>` --label '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Example VNC</span>`' --after `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dock_item_label</span>

- Remove an application from the dock given its dock label name:

`dockutil --remove '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dock_item_label</span>`'`

- Add a spacer in a section after an application:

`dockutil --add '' --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spacer|small-spacer|flex-spacer</span>` --section `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apps</span>` --after `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dock_item_label</span>

- Remove all spacer tiles:

`dockutil --remove spacer-tiles`
