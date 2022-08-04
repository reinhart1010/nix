---
layout: page
title: windows/robocopy (English)
description: "Robust File and Folder Copy."
content_hash: c0c4bda795eb81a1b752441d670c866fa155b08e
---
# robocopy

Robust File and Folder Copy.
By default files will only be copied if the source and destination have different time stamps or different file sizes.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/robocopy>.

- Copy all `.jpg` and `.bmp` files from one directory to another:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.bmp</span>

- Copy all files and subdirectories, including empty ones:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>` /E`

- Mirror/Sync a directory, deleting anything not in source and include all attributes and permissions:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>` /MIR /COPYALL`

- Copy all files and subdirectories, excluding source files that are older than destination files:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>` /E /XO`

- List all files 50 MB or larger instead of copying them:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>` /MIN:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">52428800</span>` /L`

- Allow resuming if network connection is lost and limit retries to 5 and wait time to 15 sec:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination</span>` /Z /R:5 /W:15`

- Display detailed usage information:

`robocopy /?`
