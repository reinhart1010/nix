---
layout: page
title: linux/dex (English)
description: "DesktopEntry Execution is a program to generate and execute DesktopEntry files of the Application type."
content_hash: 1787b33f7da58631ed86d0ac3f2f85ee0c8aa032
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/linux/dex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dex

DesktopEntry Execution is a program to generate and execute DesktopEntry files of the Application type.
More information: <https://github.com/jceb/dex>.

- Execute all programs in the autostart folders:

`dex --autostart`

- Execute all programs in the specified folders:

`dex --autostart --search-paths `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory3</span>`:`

- Preview the programs would be executed in a GNOME specific autostart:

`dex --autostart --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GNOME</span>

- Preview the programs would be executed in a regular autostart:

`dex --autostart --dry-run`

- Preview the value of the DesktopEntry property `Name`:

`dex --property `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.desktop</span>

- Create a DesktopEntry for a program in the current directory:

`dex --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.desktop</span>

- Execute a single program (with `Terminal=true` in the desktop file) in the given terminal:

`dex --term `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">terminal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.desktop</span>
