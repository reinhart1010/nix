---
layout: page
title: linux/tomb (English)
description: "Manage encrypted storage directories that can be safely transported and hidden in a filesystem."
content_hash: 6e14a78e852d2c7ef0cfe1cd845b8348588fb86f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tomb

Manage encrypted storage directories that can be safely transported and hidden in a filesystem.
More information: <https://www.dyne.org/software/tomb/>.

- Create a new tomb with an initial size of 100 MB:

`tomb dig -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encrypted_directory.tomb</span>

- Create a new key file that can be used to lock a tomb; user will be prompted for a password for the key:

`tomb forge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encrypted_directory.tomb.key</span>

- Forcefully create a new key, even if the tomb isn't allowing key forging (due to swap):

`tomb forge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encrypted_directory.tomb.key</span>` -f`

- Initialize and lock an empty tomb using a key made with `forge`:

`tomb lock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encrypted_directory.tomb</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encrypted_directory.tomb.key</span>

- Mount a tomb (by default in `/media`) using its key, making it usable as a regular filesystem directory:

`tomb open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encrypted_directory.tomb</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encrypted_directory.tomb.key</span>

- Close a tomb (fails if the tomb is being used by a process):

`tomb close `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encrypted_directory.tomb</span>

- Forcefully close all open tombs, killing any applications using them:

`tomb slam all`

- List all open tombs:

`tomb list`
