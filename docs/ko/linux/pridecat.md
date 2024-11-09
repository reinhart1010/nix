---
layout: page
title: linux/pridecat (한국어)
description: "cat과 유사하지만 더 다채로운 도구 :)."
content_hash: f4b498633720080f8f7c1a43fd2ca9e837c5ebf8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pridecat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pridecat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pridecat

cat과 유사하지만 더 다채로운 도구 :).
더 많은 정보: <https://github.com/lunasorcery/pridecat>.

- 파일의 내용을 프라이드 색상으로 `stdout`에 출력:

`pridecat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 내용을 트랜스 색상으로 출력:

`pridecat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">transgender|trans</span>

- 레즈비언과 양성애자 프라이드 깃발을 번갈아 사용:

`pridecat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --lesbian --bi`

- 파일의 내용을 배경색을 변경하여 출력:

`pridecat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -b`

- 디렉터리 내용을 프라이드 깃발 색상으로 나열:

`ls | pridecat --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">flag</span>
