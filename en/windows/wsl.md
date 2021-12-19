---
layout: page
title: windows/wsl (English)
description: "Manage the Windows Subsystem for Linux from the command-line."
content_hash: 2b5c02e175fe304ad1b4159ce5d364847e56955c
related_topics:
  - title: Deutsch version
    url: /de/windows/wsl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/wsl.html
    icon: bi bi-globe
---
# wsl

Manage the Windows Subsystem for Linux from the command-line.
More information: <https://docs.microsoft.com/windows/wsl/reference>.

- Start a Linux shell (in the default distribution):

`wsl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_command</span>

- Run a Linux command without using a shell:

`wsl --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Specify a particular distribution:

`wsl --distribution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_command</span>

- List available distributions:

`wsl --list`

- Export a distribution to a `.tar` file:

`wsl --export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/distro_fs.tar</span>

- Import a distribution from a `.tar` file:

`wsl --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/install_location</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/distro_fs.tar</span>

- Change the version of wsl used for the specified distribution:

`wsl --set-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Shut down Windows Subsystem for Linux:

`wsl --shutdown`
