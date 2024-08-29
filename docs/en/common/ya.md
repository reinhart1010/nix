---
layout: page
title: common/ya (English)
description: "Manage Yazi packages and plugins."
content_hash: 1ecb1b7e400bc8402b037e81f143789315919696
last_modified_at: 2024-08-29
tldri18n_status: 2
---
# ya

Manage Yazi packages and plugins.
More information: <https://github.com/sxyazi/yazi>.

- Add a package:

`ya pack -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade all packages:

`ya pack -u`

- Subscribe to messages from all remote instances:

`ya sub `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kinds</span>

- Publish a message to the current instance with string body:

`ya pub --str `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string_message</span>

- Publish a message to the current instance with JSON body:

`ya pub --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json_message</span>

- Publish a message to the specified instance with string body:

`ya pub-to --str `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">receiver</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kind</span>
