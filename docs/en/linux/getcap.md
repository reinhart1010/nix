---
layout: page
title: linux/getcap (English)
description: "Command to display the name and capabilities of each specified file."
content_hash: ca26805c85cc7ce1bfd28b7f891b412022ac8a9e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# getcap

Command to display the name and capabilities of each specified file.
More information: <https://manned.org/getcap>.

- Get capabilities for the given files:

`getcap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Get capabilities for all the files recursively under the given directories:

`getcap -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Displays all searched entries even if no capabilities are set:

`getcap -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
