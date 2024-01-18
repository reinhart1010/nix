---
layout: page
title: osx/dockutil (English)
description: "Manage macOS dock items."
content_hash: 04b7fe3d86234c1aca10873c52e4cd2b487887cf
last_modified_at: 2024-01-18
tldri18n_status: 2
---
# dockutil

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
