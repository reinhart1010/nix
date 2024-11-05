---
layout: page
title: common/nkf (한국어)
description: "네트워크 한자 필터: 한자 코드를 하나의 인코딩에서 다른 인코딩으로 변환."
content_hash: 19751a6a3a582a7f34395598cb81df4e3fc94546
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nkf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nkf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nkf

네트워크 한자 필터: 한자 코드를 하나의 인코딩에서 다른 인코딩으로 변환.
더 많은 정보: <https://manned.org/nkf>.

- UTF-8 인코딩으로 변환:

`nkf -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- SHIFT_JIS 인코딩으로 변환:

`nkf -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- UTF-8 인코딩으로 변환하고 파일 덮어쓰기:

`nkf -w --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- LF를 새 줄 코드로 사용하고 덮어쓰기 (UNIX 타입):

`nkf -d --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- CRLF를 새 줄 코드로 사용하고 덮어쓰기 (Windows 타입):

`nkf -c --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- MIME 파일을 해독하고 덮어쓰기:

`nkf -m --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>
