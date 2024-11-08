---
layout: page
title: linux/dos2unix (한국어)
description: "DOS 스타일의 줄 바꿈을 Unix 스타일로 변경."
content_hash: 24de0fb1d5b2750a7c7470b8800cf2af0b6d8727
last_modified_at: 2024-11-08
related_topics:
  - title: català version
    url: /ca/linux/dos2unix.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dos2unix.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dos2unix.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/dos2unix.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dos2unix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dos2unix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dos2unix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dos2unix

DOS 스타일의 줄 바꿈을 Unix 스타일로 변경.
CRLF를 LF로 대체합니다.
같이 보기: `unix2dos`, `unix2mac`, `mac2unix`.
더 많은 정보: <https://manned.org/dos2unix>.

- 파일의 줄 바꿈 변경:

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- Unix 스타일의 줄 바꿈으로 복사본 생성:

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--newfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새_파일</span>

- 파일 정보 표시:

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--info</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 바이트 순서 표시(BOM) 유지/추가/제거:

`dos2unix --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
