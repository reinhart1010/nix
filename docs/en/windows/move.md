---
layout: page
title: windows/move (English)
description: "Move or rename files and directories."
content_hash: ae02fc15fdea4092eb5a5fe6ca4d1ae416da5e28
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# move

Move or rename files and directories.
In PowerShell, this command is an alias of `Move-Item`. This documentation is based on the Command Prompt (`cmd`) version of `move`.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/move>.

- View documentation of the equivalent PowerShell command:

`tldr move-item`

- Rename a file or directory when the target is not an existing directory:

`move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\target</span>

- Move a file or directory into an existing directory:

`move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\existing_directory</span>

- Move a file or directory across drives:

`move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\path\to\source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">D:\path\to\target</span>

- Do not prompt for confirmation before overwriting existing files:

`move /Y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\existing_directory</span>

- Prompt for confirmation before overwriting existing files, regardless of file permissions:

`move /-Y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\existing_directory</span>
