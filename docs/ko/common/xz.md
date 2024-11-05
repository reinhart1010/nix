---
layout: page
title: common/xz (한국어)
description: "XZ 및 LZMA 파일을 압축 또는 해제."
content_hash: ad35204980d5847d8a1c347d943becd80590f05e
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xz.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/xz.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/xz.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/xz.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/xz.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xz.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xz

XZ 및 LZMA 파일을 압축 또는 해제.
더 많은 정보: <https://manned.org/xz>.

- 파일을 xz로 압축:

`xz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- XZ 파일 압축 해제:

`xz --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.xz</span>

- 파일을 lzma로 압축:

`xz --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- LZMA 파일 압축 해제:

`xz --decompress --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.lzma</span>

- 파일 압축 해제 후 `stdout`에 쓰기 (`--keep` 포함):

`xz --decompress --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.xz</span>

- 파일을 압축하지만 원본을 삭제하지 않기:

`xz --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 가장 빠른 압축으로 파일 압축:

`xz -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 최고의 압축으로 파일 압축:

`xz -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
