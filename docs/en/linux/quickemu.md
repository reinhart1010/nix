---
layout: page
title: linux/quickemu (English)
description: "Build and manage highly optimised desktop virtual machines quickly."
content_hash: e107f016bbd569ec68da21703f0819c4e1fc10ea
last_modified_at: 2024-01-22
tldri18n_status: 2
---
# quickemu

Build and manage highly optimised desktop virtual machines quickly.
See also: `quickget`, for preparing VM configurations.
More information: <https://github.com/quickemu-project/quickemu>.

- Create and run a virtual machine from a configuration file:

`quickemu --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.conf</span>

- Do not commit any changes to disk/snapshot but write any changes to temporary files:

`quickemu --status-quo --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.conf</span>

- Start the virtual machine in full-screen mode (<Ctrl> + <Alt> + f to exit) and select the display backend (`sdl` by default):

`quickemu --fullscreen --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdl|gtk|spice|spice-app|none</span>` --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.conf</span>

- Select a virtual audio device to emulate and create a desktop shortcut:

`quickemu --sound-card `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">intel-hda|ac97|es1370|sb16|none</span>` --shortcut --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.conf</span>

- Create a snapshot:

`quickemu --snapshot create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.conf</span>

- Restore a snapshot:

`quickemu --snapshot apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.conf</span>

- Delete a snapshot:

`quickemu --snapshot delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.conf</span>
