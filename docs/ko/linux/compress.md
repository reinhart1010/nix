---
layout: page
title: linux/compress (한국어)
description: "Unix `compress` 명령어를 사용하여 파일 압축."
content_hash: 601249a4c598c3f6218a1b8a05ad0bd4acc04368
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/compress.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/compress.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># compress

Unix `compress` 명령어를 사용하여 파일 압축.
더 많은 정보: <https://manned.org/compress.1>.

- 특정 파일 압축:

`compress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 파일 압축, 존재하지 않는 파일은 무시:

`compress -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 최대 압축 비트 지정 (9-16 비트):

`compress -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비트</span>

- `stdout`에 기록 (파일은 변경되지 않음):

`compress -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 압축 해제 (`uncompress`처럼 동작):

`compress -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 압축 비율 표시:

`compress -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
