---
layout: page
title: common/xdg-user-dirs-update (English)
description: "Update XDG user directories."
content_hash: 951adfcb065e09c7a2e976c125c73f4bc62acae4
---
# xdg-user-dirs-update

Update XDG user directories.
More information: <https://manpages.ubuntu.com/manpages/bionic/man1/xdg-user-dirs-update.1.html>.

- Change XDG's DESKTOP directory to the specified directory (must be absolute):

`xdg-user-dirs-update --set DESKTOP "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`"`

- Write the result to the specified dry-run-file instead of the `user-dirs.dirs` file:

`xdg-user-dirs-update --dummy-output "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dry_run_file</span>`" --set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xdg_user_directory</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`"`
