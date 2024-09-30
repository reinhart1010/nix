---
layout: page
title: common/cavif (한국어)
description: "PNG/JPEG 이미지를 AVIF로 변환함. Rust로 작성됨."
content_hash: e0259fe01dde821c7f96588ce04b6f94265c7d4f
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/cavif.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cavif

PNG/JPEG 이미지를 AVIF로 변환함. Rust로 작성됨.
참고: `convert`.
더 많은 정보: <https://github.com/kornelski/cavif-rs>.

- JPEG 파일을 AVIF로 변환하여, `file.avif`에 저장:

`cavif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.jpg</span>

- 이미지를 품질을 조정하고 PNG 파일을 AVIF로 변환:

`cavif --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.png</span>

- 출력 위치를 지정:

`cavif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.jpg</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.avif</span>

- 이미 존재하는 경우, 대상 파일을 덮어씀:

`cavif --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.jpg</span>
