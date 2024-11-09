---
layout: page
title: linux/avifenc (한국어)
description: "AV1 이미지 파일 포맷 (AVIF) 인코더."
content_hash: e682d4b0f15547b4b21088229576fc21f56d6933
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/avifenc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# avifenc

AV1 이미지 파일 포맷 (AVIF) 인코더.
더 많은 정보: <https://aomediacodec.github.io/av1-avif/>.

- 특정 PNG 이미지를 AVIF로 변환:

`avifenc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.avif</span>

- 특정 속도로 인코딩 (6=기본, 0=가장 느림, 10=가장 빠름):

`avifenc --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.avif</span>
