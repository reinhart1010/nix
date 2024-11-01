---
layout: page
title: common/zipnote (한국어)
description: "Zip 압축 파일의 주석을 보고, 추가하거나 편집."
content_hash: f61bddb5b3fecdb4b74ae12644069d1377dec188
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zipnote.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zipnote.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zipnote

Zip 압축 파일의 주석을 보고, 추가하거나 편집.
Zip 압축 파일에서 파일 이름도 변경 가능.
더 많은 정보: <https://manned.org/zipnote>.

- Zip 압축 파일의 주석 보기:

`zipnote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zip</span>

- Zip 압축 파일의 주석을 파일로 추출:

`zipnote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zip</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 파일에서 주석을 추가/업데이트하여 Zip 압축 파일에 반영:

`zipnote -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zip</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>
