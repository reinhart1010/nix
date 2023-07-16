---
layout: page
title: common/grpcurl (English)
description: "Interact with gRPC servers."
content_hash: 116af83e616874e544457e1f0275ca6860d15c9b
last_modified_at: 2023-07-16
---
# grpcurl

Interact with gRPC servers.
Like `curl`, but for gRPC.
More information: <https://github.com/fullstorydev/grpcurl>.

- Send an empty request:

`grpcurl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grpc.server.com:443</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my.custom.server.Service/Method</span>

- Send a request with a header and a body:

`grpcurl -H "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Authorization: Bearer $token</span>`" -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"foo": "bar"}'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grpc.server.com:443</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my.custom.server.Service/Method</span>

- List all services exposed by a server:

`grpcurl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grpc.server.com:443</span>` list`

- List all methods in a particular service:

`grpcurl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grpc.server.com:443</span>` list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my.custom.server.Service</span>
