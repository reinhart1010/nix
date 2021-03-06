---
layout: page
title: common/kitex (English)
description: "Code generation tool provided by the Go RPC framework Kitex."
content_hash: 8cb68df462e761a3a6b223f6b61041b59702c301
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kitex

Code generation tool provided by the Go RPC framework Kitex.
Kitex accepts both thrift and protobuf IDLs, and supports generating a skeleton of a server side project.
More information: <https://www.cloudwego.io>.

- Generate client codes when a project is in `$GOPATH`:

`kitex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/IDL_file.thrift</span>

- Generate client codes when a project is not in `$GOPATH`:

` kitex -module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github.com/xx-org/xx-name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/IDL_file.thrift</span>

- Generate client codes with protobuf IDL:

`kitex -type protobuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/IDL_file.proto</span>

- Generate server codes:

`kitex -service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svc_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/IDL_file.thrift</span>
