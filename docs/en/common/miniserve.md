---
layout: page
title: common/miniserve (English)
description: "Simple HTTP file server."
content_hash: 463707473f9a20dcca1fc13d86d4a001338b3efa
last_modified_at: 2023-07-16
---
# miniserve

Simple HTTP file server.
More information: <https://github.com/svenstaro/miniserve>.

- Serve a directory:

`miniserve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Serve a single file:

`miniserve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Serve a directory using HTTP basic authentication:

`miniserve --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
