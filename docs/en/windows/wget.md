---
layout: page
title: windows/wget (English)
description: "In PowerShell, this command may be an alias of `Invoke-WebRequest` when the original `wget` program (<https://www.gnu.org/software/wget>) is not properly installed."
content_hash: 6463f690ba0f659aa157ba209f14f463e15661c4
related_topics:
  - title: Indonesia version
    url: /id/windows/wget.html
    icon: bi bi-globe
---
# wget

In PowerShell, this command may be an alias of `Invoke-WebRequest` when the original `wget` program (<https://www.gnu.org/software/wget>) is not properly installed.

- Check whether `wget` is properly installed by printing its version number. If this command evaluates into an error, PowerShell may have substituted this command with `Invoke-WebRequest`:

`curl --version`

- View documentation for the original `wget` command:

`tldr wget -p common`

- View documentation for the original `wget` command in older versions of `tldr` command-line client:

`tldr wget -o common`

- View documentation for PowerShell's `Invoke-WebRequest` command:

`tldr invoke-webrequest`
