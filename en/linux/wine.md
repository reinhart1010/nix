---
layout: page
title: linux/wine (English)
description: "Run Windows executables on Unix-based systems."
content_hash: d0b668459797fcf15c9ea05c5fa69f12ca2c2486
---
# wine

Run Windows executables on Unix-based systems.
More information: <https://wiki.winehq.org/>.

- Run a specific program inside the `wine` environment:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a specific program in background:

`wine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Install/uninstall an MSI package:

`wine msiexec /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i|x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.msi</span>

- Run `File Explorer`, `Notepad`, or `WordPad`:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">explorer|notepad|write</span>

- Run `Registry Editor`, `Control Panel`, or `Task Manager`:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regedit|control|taskmgr</span>

- Run the configuration tool:

`wine winecfg`
