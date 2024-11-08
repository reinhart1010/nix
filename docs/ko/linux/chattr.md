---
layout: page
title: linux/chattr (한국어)
description: "파일 또는 디렉토리의 속성 변경."
content_hash: 826dd2c90f025ccace5dae44f7af7d648f4afd15
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/chattr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/chattr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/chattr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chattr

파일 또는 디렉토리의 속성 변경.
더 많은 정보: <https://manned.org/chattr>.

- 파일 또는 디렉토리를 변경 및 삭제 불가능하도록 설정 (슈퍼유저도 포함):

`chattr +i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 파일 또는 디렉토리를 변경 가능하도록 설정:

`chattr -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 전체 디렉토리와 그 내용을 재귀적으로 변경 및 삭제 불가능하도록 설정:

`chattr -R +i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
