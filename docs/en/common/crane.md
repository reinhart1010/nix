---
layout: page
title: common/crane (English)
description: "Container images managing tool."
content_hash: 0ef3487bc7ed7ac092df7633d71db92703505bf0
last_modified_at: 2024-10-26
related_topics:
  - title: 한국어 version
    url: /ko/common/crane.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane

Container images managing tool.
Some subcommands such as `pull`, `push`, `copy`, etc. have their own usage documentation.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>.

- Execute a `crane` subcommand:

`crane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Allow pushing non-distributable (foreign) layers:

`crane --allow-nondistributable-artifacts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Allow image references to be fetched without TLS:

`crane --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Specify the platform in the form os/arch`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/variant</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:osversion</span>` (e.g. linux/amd64). (default all):

`crane --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Enable debug logs for a subcommand:

`crane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Display help for a subcommand:

`crane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>
