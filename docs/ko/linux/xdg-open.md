---
layout: page
title: linux/xdg-open (한국어)
description: "사용자 선호 응용 프로그램에서 파일이나 URL 열기."
content_hash: 0b621429bcc0ad43469a6b69643dccf41344fdb4
last_modified_at: 2024-10-29
related_topics:
  - title: català version
    url: /ca/linux/xdg-open.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/xdg-open.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/xdg-open.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xdg-open.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xdg-open

사용자 선호 응용 프로그램에서 파일이나 URL 열기.
더 많은 정보: <https://portland.freedesktop.org/doc/xdg-open.html>.

- 기본 파일 탐색기에서 현재 디렉터리 열기:

`xdg-open .`

- 기본 브라우저에서 URL 열기:

`xdg-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 기본 이미지 뷰어에서 이미지 열기:

`xdg-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- 기본 PDF 뷰어에서 PDF 열기:

`xdg-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pdf</span>

- 도움말 표시:

`xdg-open --help`
