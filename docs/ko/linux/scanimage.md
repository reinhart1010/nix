---
layout: page
title: linux/scanimage (한국어)
description: "Scanner Access Now Easy API를 사용하여 이미지를 스캔."
content_hash: a14806f86ee53d269851c794126a7f69f3381c40
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/scanimage.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/scanimage.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># scanimage

Scanner Access Now Easy API를 사용하여 이미지를 스캔.
더 많은 정보: <http://sane-project.org/man/scanimage.1.html>.

- 사용 가능한 스캐너를 나열하여 대상 장치가 연결되고 인식되었는지 확인:

`scanimage -L`

- 이미지를 스캔하여 파일로 저장:

`scanimage --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pnm|tiff|png|jpeg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새_이미지</span>
