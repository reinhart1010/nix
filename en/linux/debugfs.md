---
layout: page
title: linux/debugfs (English)
description: "An interactive ext2/ext3/ext4 filesystem debugger."
content_hash: b251a618aa4730004dd01de644c96333d33dab2b
---
# debugfs

An interactive ext2/ext3/ext4 filesystem debugger.
More information: <https://manned.org/debugfs>.

- Open the filesystem in read only mode:

`debugfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Open the filesystem in read write mode:

`debugfs -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Read commands from a specified file, execute them and then exit:

`debugfs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cmd_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- View the filesystem stats in debugfs console:

`stats`

- Close the filesystem:

`close -a`

- List all available commands:

`lr`
