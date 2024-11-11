---
layout: page
title: linux/genisoimage (한국어)
description: "ISO9660/Joliet/HFS 하이브리드 파일 시스템을 생성하는 프리마스터링 프로그램."
content_hash: 1cb8f8c6afb87c599b5da44d5302ee96a4f7d904
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/genisoimage.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/genisoimage.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/genisoimage.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># genisoimage

ISO9660/Joliet/HFS 하이브리드 파일 시스템을 생성하는 프리마스터링 프로그램.
더 많은 정보: <https://manned.org/genisoimage.1>.

- 주어진 소스 디렉토리에서 ISO 이미지 생성:

`genisoimage -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내_이미지.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_폴더</span>

- ISO9660 파일 시스템에 대해 작은 겉보기 크기를 보고하여 2GiB보다 큰 파일을 포함한 ISO 이미지 생성:

`genisoimage -o -allow-limited-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내_이미지.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_폴더</span>
