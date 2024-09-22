---
layout: page
title: common/brotli (한국어)
description: "Brotli 압축을 사용하여 파일을 압축/압축 해제."
content_hash: b13e58309c8d3ffa6be83c077567a1f54d9f21da
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/brotli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brotli

Brotli 압축을 사용하여 파일을 압축/압축 해제.
더 많은 정보: <https://github.com/google/brotli>.

- 파일을 압축하여 파일 옆에 압축 버전을 생성:

`brotli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 압축 해제([d]ecompress)하여, 파일 옆에 압축되지 않은 버전을 생성:

`brotli -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.br</span>

- 출력([o]utput) 파일 이름을 지정하여, 파일을 압축:

`brotli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_출력_파일.br</span>

- 출력([o]utput) 파일 이름을 지정하여 Brotli 파일을 압축 해제([d]ecompress)ㄴ:

`brotli -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_파일.br</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 압축 품질을 지정 (1=가장 빠름 (가장 안 좋은 품질), 11=가장 느림 (가장 좋은 품질)):

`brotli -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">11</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축된_출력_파일.br</span>
