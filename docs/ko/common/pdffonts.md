---
layout: page
title: common/pdffonts (한국어)
description: "Portable Document Format (PDF) 파일의 폰트 정보 뷰어."
content_hash: 6f4b1a2c1dacf00b9d524afcd4e37b91c5f7b7ae
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/pdffonts.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pdffonts.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdffonts

Portable Document Format (PDF) 파일의 폰트 정보 뷰어.
더 많은 정보: <https://www.xpdfreader.com/pdffonts-man.html>.

- PDF 파일의 폰트 정보 출력:

`pdffonts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- PDF 파일의 보안 제한을 우회하기 위해 사용자 비밀번호 지정:

`pdffonts -upw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- PDF 파일의 보안 제한을 우회하기 위해 소유자 비밀번호 지정:

`pdffonts -opw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- PDF 파일이 래스터화될 때 사용될 폰트의 위치에 대한 추가 정보 출력:

`pdffonts -loc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- PDF 파일이 PostScript로 변환될 때 사용될 폰트의 위치에 대한 추가 정보 출력:

`pdffonts -locPS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>
