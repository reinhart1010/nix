---
layout: page
title: common/cavif (한국어)
description: "PNG/JPEG 이미지를 AVIF로 변환함. Rust로 작성됨."
content_hash: e0259fe01dde821c7f96588ce04b6f94265c7d4f
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/common/cavif.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cavif.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cavif

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
