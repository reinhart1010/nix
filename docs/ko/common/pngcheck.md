---
layout: page
title: common/pngcheck (한국어)
description: "PNG, JNG, MNG 파일에 대한 자세한 정보를 출력하고 검증합니다."
content_hash: 08ed0f06a96312346c3a550f431a4a81800ef2cd
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pngcheck.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pngcheck.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pngcheck.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pngcheck

PNG, JNG, MNG 파일에 대한 자세한 정보를 출력하고 검증합니다.
더 많은 정보: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- 이미지의 요약 정보 출력 (너비, 높이, 색상 깊이):

`pngcheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>

- [c]색상화된 출력으로 이미지 정보 출력:

`pngcheck -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>

- 이미지에 대한 [v]erbose 정보 출력:

`pngcheck -cvt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>

- `stdin`에서 이미지를 받아와 자세한 정보 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>` | pngcheck -cvt`

- 특정 파일 내에서 PNG를 [s]검색하여 정보 출력:

`pngcheck -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>

- 다른 파일 내에서 PNG를 검색하고 [x]추출:

`pngcheck -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.png</span>
