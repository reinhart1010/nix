---
layout: page
title: linux/cloud-init (English)
description: "Command line tool for managing cloud instance initialization."
content_hash: 59433dbeaf852388daf6daba5a80a1ebf6272284
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cloud-init

Command line tool for managing cloud instance initialization.
More information: <https://cloudinit.readthedocs.io>.

- Display the status of the most recent cloud-init run:

`cloud-init status`

- Wait for cloud-init to finish running and then report status:

`cloud-init status --wait`

- List available top-level metadata keys to query:

`cloud-init query --list-keys`

- Query cached instance metadata for data:

`cloud-init query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dot_delimited_variable_path</span>

- Clean logs and artifacts to allow cloud-init to rerun:

`cloud-init clean`
