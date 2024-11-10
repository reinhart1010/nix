---
layout: page
title: linux/qrcp (한국어)
description: "파일 전송 도구."
content_hash: 434700ffe7f2f1d3afee4696e8f3488b842f0252
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/qrcp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qrcp

파일 전송 도구.
더 많은 정보: <https://github.com/claudiodangelis/qrcp>.

- 파일 또는 폴더 전송:

`qrcp send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더 경로/대상/파일_폴더 ...</span>

- 파일 수신:

`qrcp receive`

- 전송 전 콘텐츠 압축:

`qrcp send --zip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 특정 [p]포트 사용:

`qrcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">send|receive</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트_번호</span>

- 특정 네트워크 [i]인터페이스 사용:

`qrcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">send|receive</span>` --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 서버를 계속 활성 상태로 유지:

`qrcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">send|receive</span>` --keep-alive`
