---
layout: page
title: common/libreoffice (한국어)
description: "강력하고 무료인 오피스 제품군 LibreOffice의 CLI."
content_hash: c8364041262da82fe95e6f0768497e1c0ffbdf5a
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/libreoffice.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/libreoffice.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/libreoffice.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># libreoffice

강력하고 무료인 오피스 제품군 LibreOffice의 CLI.
더 많은 정보: <https://www.libreoffice.org/>.

- 하나 이상의 파일을 읽기 전용 모드로 열기:

`libreoffice --view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 하나 이상의 파일 내용 표시:

`libreoffice --cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 프린터를 사용하여 파일 인쇄:

`libreoffice --pt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 현재 디렉터리의 모든 `.doc` 파일을 PDF로 변환:

`libreoffice --convert-to pdf *.doc`
