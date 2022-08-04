---
layout: page
title: common/grpcurl (English)
description: "Like cURL, but for gRPC: CLI tool for interacting with gRPC servers."
content_hash: 116e1d3c24ee1e524e42907cc240c84c04d2174c
---
# grpcurl

Like cURL, but for gRPC: CLI tool for interacting with gRPC servers.
More information: <https://github.com/fullstorydev/grpcurl>.

- Send an empty request:

`grpcurl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grpc.server.com:443</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my.custom.server.Service/Method</span>

- Send a request with a header and a body:

`grpcurl -H "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Authorization: Bearer $token</span>`" -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"foo": "bar"}'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grpc.server.com:443</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my.custom.server.Service/Method</span>

- List all services exposed by a server:

`grpcurl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grpc.server.com:443</span>` list`

- List all methods in a particular service:

`grpcurl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grpc.server.com:443</span>` list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my.custom.server.Service</span>
