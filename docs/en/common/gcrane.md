---
layout: page
title: common/gcrane (English)
description: "Container images managing tool."
content_hash: 9ed9d77a9c428801535e622a487583ed18d028f8
last_modified_at: 2024-10-16
tldri18n_status: 2
---
# gcrane

Container images managing tool.
This tool implements a superset of the `crane` commands, with additional commands that are specific to `gcr.io`.
Some subcommands such as `append`, `auth`, `copy`, etc. have their own usage documentation which can be found under `crane`.
Some subcommands such as `completion`, `gc`, `help` are specific to gcrane and have their own usage documentation.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Execute a `gcrane` subcommand:

`gcrane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Allow pushing non-distributable (foreign) layers:

`gcrane --allow-nondistributable-artifacts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Allow image references to be fetched without TLS:

`gcrane --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Specify the platform in the form os/arch`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/variant</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:osversion</span>` (e.g. linux/amd64). (default all):

`gcrane --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Enable debug logs:

`gcrane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Display help:

`gcrane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
