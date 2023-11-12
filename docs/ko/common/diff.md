---
layout: page
title: common/diff (한국어)
description: "파일들과 디렉토리들을 비교한다."
content_hash: 0dc1d97a871230697e7bed15ee8ffba42211cc13
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/diff.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/diff.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/diff.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/diff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/diff.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/diff.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/diff.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># diff

파일들과 디렉토리들을 비교한다.
더 많은 정보: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- 파일들 비교하기 (`이전_파일명`을 `새_파일명`으로 바꾸는 변경점들 목록):

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이전_파일명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_파일명</span>

- 공백들을 무시하고, 파일들 비교하기:

`diff -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이전_파일명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_파일명</span>

- 차이점들을 나란히 보여주는 파일들 비교하기:

`diff -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이전_파일명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_파일명</span>

- 통합된 포맷의 차이점들 표시하며 파일들 비교하기 (`git diff`에서 사용되는 것 같이):

`diff -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이전_파일명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_파일명</span>

- 재귀적으로 디렉토리들 비교하기 (다른 파일/디렉토리들의 이름 및 파일에 대한 변경점 출력):

`diff -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이전_디렉토리명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_디렉토리명</span>

- 디렉토리들을 비교하고, 서로 다른 파일이름만 표시하기:

`diff -rq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이전_디렉토리명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_디렉토리명</span>
