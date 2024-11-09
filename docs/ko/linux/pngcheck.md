---
layout: page
title: linux/pngcheck (한국어)
description: "PNG 기반(PNG, JNG, MNG) 이미지 파일의 무결성을 검증하는 포렌식 도구."
content_hash: bd2aefe55f370752d0f32843d36ae06277986141
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pngcheck.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/pngcheck.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pngcheck.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pngcheck

PNG 기반(PNG, JNG, MNG) 이미지 파일의 무결성을 검증하는 포렌식 도구.
파일에서 내장된 이미지와 텍스트를 추출할 수도 있습니다.
더 많은 정보: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- 이미지 파일의 무결성 검증:

`pngcheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- [v]자세히 및 [c]olorized 출력으로 파일 확인:

`pngcheck -vc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- [t]ext 청크 내용 표시 및 특정 파일 내의 PNG 검색:

`pngcheck -ts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 특정 파일 내에 내장된 PNG 검색 및 e[x]tract 추출:

`pngcheck -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>
