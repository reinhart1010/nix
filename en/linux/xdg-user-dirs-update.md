---
layout: page
title: linux/xdg-user-dirs-update (English)
description: "Update XDG user directories."
content_hash: e6cbb1473716756ec540d81c1667c4554c081dee
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xdg-user-dirs-update

Update XDG user directories.
More information: <https://manned.org/xdg-user-dirs-update>.

- Change XDG's DESKTOP directory to the specified directory (must be absolute):

`xdg-user-dirs-update --set DESKTOP "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`"`

- Write the result to the specified dry-run-file instead of the `user-dirs.dirs` file:

`xdg-user-dirs-update --dummy-output "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dry_run_file</span>`" --set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xdg_user_directory</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`"`
