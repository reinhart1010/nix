---
layout: page
title: common/gladtex (한국어)
description: "HTML 파일용 LaTeX 수식 전처리기."
content_hash: c642cc9f6c6423198e6fcb52fff3c23c487c0dd3
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gladtex.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gladtex.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gladtex

HTML 파일용 LaTeX 수식 전처리기.
LaTeX 수식을 이미지로 변환.
더 많은 정보: <https://manned.org/gladtex.1>.

- HTML로 변환:

`gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.htex</span>

- 변환된 파일을 특정 위치에 저장:

`gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.htex</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.html</span>

- 생성된 이미지를 특정 디렉토리([d]irectory)에 저장:

`gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.htex</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지_출력_디렉토리</span>

- 이미지 해상도([r]esolution) 설정 (dpi 단위, 기본값은 100):

`gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.htex</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resolution</span>

- 변환 후 LaTeX 파일 유지([k]eep) :

`gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.htex</span>` -k`

- 이미지의 배경([b]ackground) 및 전경([f]oreground)색 설정:

`gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.htex</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배경_색</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전경_색</span>

- `pandoc` 및 `gladtex`를 사용하여 마크다운을 HTML로 변환:

`pandoc -s -t html --gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.md</span>` | gladtex -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.html</span>
