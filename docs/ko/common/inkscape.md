---
layout: page
title: common/inkscape (한국어)
description: "SVG (Scalable Vector Graphics) 편집 프로그램."
content_hash: d087c6202dac93d9757464933345b4a41f651327
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/inkscape.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/inkscape.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/inkscape.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># inkscape

SVG (Scalable Vector Graphics) 편집 프로그램.
Inkscape 버전 0.92.x 이하의 경우, -o 대신 -e를 사용하세요.
더 많은 정보: <https://inkscape.org>.

- Inkscape GUI에서 SVG 파일을 열기:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.svg</span>

- 기본 형식(PNG) 및 기본 해상도(96 DPI)를 사용하여 SVG 파일을 비트맵으로 내보냄:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.png</span>

- SVG 파일을 600x400 픽셀의 비트맵으로 내보내기 (가로와 세로 사이의 비율 왜곡이 발생할 수 있음):

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.png</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">600</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">400</span>

- SVG 파일의 그림(모든 객체의 경계가 있는 상자)을 비트맵으로 내보냄:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.png</span>` -D`

- 해당 ID가 지정된 단일 객체를 비트맵으로 내보냄:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.svg</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object.png</span>

- SVG 문서를 PDF로 내보내고 모든 텍스트를 경로로 변경:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.pdf</span>` --export-text-to-path`

- id="path123"로 객체를 복제하고, 복사본을 90도로 회전한 다음, 파일을 저장하고, Inkscape를 종료:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.svg</span>` --select=path123 --verb="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">EditDuplicate;ObjectRotate90;FileSave;FileQuit</span>`"`
