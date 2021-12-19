---
layout: page
title: common/miniserve (English)
description: "Simple HTTP file server CLI."
content_hash: 9b8fdc981df348d284206a99558bfad920b24561
---
# miniserve

Simple HTTP file server CLI.
More information: <https://github.com/svenstaro/miniserve>.

- Serve a directory:

`miniserve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Serve a single file:

`miniserve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Serve a directory using HTTP basic authentication:

`miniserve --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
