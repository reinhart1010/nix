---
layout: page
title: common/pdfinfo (한국어)
description: "Portable Document Format (PDF) 파일 정보 뷰어."
content_hash: 2c25e22a3319bd1c22586d4f89ae529b7cf911ec
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/pdfinfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pdfinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdfinfo

Portable Document Format (PDF) 파일 정보 뷰어.
더 많은 정보: <https://www.xpdfreader.com/pdfinfo-man.html>.

- PDF 파일 정보 출력:

`pdfinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- 보안 제한을 우회하기 위해 PDF 파일의 사용자 비밀번호 지정:

`pdfinfo -upw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- 보안 제한을 우회하기 위해 PDF 파일의 소유자 비밀번호 지정:

`pdfinfo -opw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>
