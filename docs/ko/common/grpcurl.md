---
layout: page
title: common/grpcurl (한국어)
description: "gRPC 서버와 상호 작용."
content_hash: 5b1374e08e0e08482c32de872cfd7868ac43b5f3
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/grpcurl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grpcurl

gRPC 서버와 상호 작용.
`curl`과 비슷하지만, gRPC용임.
더 많은 정보: <https://github.com/fullstorydev/grpcurl>.

- 빈 요청 보내기:

`grpcurl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grpc.server.com:443</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my.custom.server.Service/Method</span>

- 헤더와 본문이 포함된 요청을 보냄:

`grpcurl -H "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Authorization: Bearer $token</span>`" -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"foo": "bar"}'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grpc.server.com:443</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my.custom.server.Service/Method</span>

- 서버가 노출하는 모든 서비스를 나열:

`grpcurl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grpc.server.com:443</span>` list`

- 특정 서비스의 모든 메서드를 나열:

`grpcurl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grpc.server.com:443</span>` list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my.custom.server.Service</span>
