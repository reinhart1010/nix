---
layout: page
title: common/gixy (한국어)
description: "nginx 구성 파일 분석."
content_hash: b4d07045e909f2d5f44db8adf1356efebc4a5b52
last_modified_at: 2024-10-24
related_topics:
  - title: English version
    url: /en/common/gixy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gixy

nginx 구성 파일 분석.
더 많은 정보: <https://github.com/yandex/gixy>.

- nginx 구성 파일 분석 (기본 경로: `/etc/nginx/nginx.conf`):

`gixy`

- nginx 구성 분석하지만 특정 테스트 넘어감:

`gixy --skips `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http_splitting</span>

- 특정 세부 수준으로 nginx 구성을 분석:

`gixy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|-ll|-lll</span>

- 특정 경로에서 nginx 구성 파일을 분석:

`gixy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일_2</span>
