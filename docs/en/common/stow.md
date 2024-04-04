---
layout: page
title: common/stow (English)
description: "Symlink manager."
content_hash: c04de3e52779741e160a39b457ae7e57b1a8c6b5
last_modified_at: 2024-04-04
tldri18n_status: 2
---
# stow

Symlink manager.
Often used to manage dotfiles.
See also: `chezmoi`, `tuckr`, `vcsh`, `homeshick`.
More information: <https://www.gnu.org/software/stow>.

- Symlink all files recursively to a given directory:

`stow --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 directory1 file2 directory2</span>

- Delete symlinks recursively from a given directory:

`stow --delete --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 directory1 file2 directory2</span>

- Simulate to see what the result would be like:

`stow --simulate --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 directory1 file2 directory2</span>

- Delete and resymlink:

`stow --restow --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 directory1 file2 directory2</span>

- Exclude files matching a regular expression:

`stow --ignore=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>` --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 directory1 file2 directory2</span>
