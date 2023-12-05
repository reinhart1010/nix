---
layout: page
title: linux/ripmime (English)
description: "Extract attachments out of a MIME encoded email package."
content_hash: 8be0fc8e553e2933981cb13ce68958613bfe166d
last_modified_at: 2023-12-05
tldri18n_status: 2
---
# ripmime

Extract attachments out of a MIME encoded email package.
More information: <https://pldaniels.com/ripmime>.

- Extract file contents in the current directory:

`ripmime -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Extract file contents in a specific directory:

`ripmime -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Extract file contents and print verbose output:

`ripmime -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -v`

- Get detailed information about the whole decoding process:

`ripmime -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --debug`
