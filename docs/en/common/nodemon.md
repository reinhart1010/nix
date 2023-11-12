---
layout: page
title: common/nodemon (English)
description: "Watch files and automatically restart a node application when changes are detected."
content_hash: 3f25bba855db0472d0d55f73da34cac0d989c315
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/nodemon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nodemon

Watch files and automatically restart a node application when changes are detected.
More information: <https://nodemon.io>.

- Execute the specified file and watch a specific file for changes:

`nodemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Manually restart nodemon (note nodemon must already be active for this to work):

`rs`

- Ignore specific files:

`nodemon --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Pass arguments to the node application:

`nodemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Pass arguments to node itself if they're not nodemon arguments already (e.g. `--inspect`):

`nodemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Run an arbitrary non-node script:

`nodemon --exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_to_run_script</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script</span>

- Run a Python script:

`nodemon --exec "python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>
