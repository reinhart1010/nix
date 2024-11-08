---
layout: page
title: common/mitmdump (한국어)
description: "HTTP 트래픽을 보기, 기록 및 프로그래밍적으로 변환."
content_hash: dfe2c02d9653335188f3d1ce30f9a34821f0819b
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mitmdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mitmdump

HTTP 트래픽을 보기, 기록 및 프로그래밍적으로 변환.
mitmproxy의 명령줄 대응 도구.
더 많은 정보: <https://docs.mitmproxy.org/stable/#mitmdump>.

- 프록시를 시작하고 모든 출력을 파일에 저장:

`mitmdump -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 저장된 트래픽 파일에서 POST 요청만 필터링:

`mitmdump -nr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일_이름</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일_이름</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~m post</span>`"`

- 저장된 트래픽 파일 재생:

`mitmdump -nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
