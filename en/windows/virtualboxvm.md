---
layout: page
title: windows/virtualboxvm (English)
description: "The VirtualBox virtual machine management CLI."
content_hash: af62b40442073a63f100a37cac189f99738cfd55
---
# virtualboxvm

The VirtualBox virtual machine management CLI.
More information: <https://www.virtualbox.org>.

- Start a virtual machine:

`virtualboxvm --startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>

- Start a virtual machine in fullscreen mode:

`virtualboxvm --startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>` --fullscreen`

- Mount the specified DVD image file:

`virtualboxvm --startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>` --dvd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>

- Display a command-line window with debug information:

`virtualboxvm --startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>` --debug-command-line`

- Start a virtual machine in a paused state:

`virtualboxvm --startvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|uuid</span>` --start-paused`
