---
layout: page
title: linux/cat (한국어)
description: "[f]파일을 출력하고 연결."
content_hash: 54e6a33e9bd0bc5eff613a6b4c22a84cee38ca01
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/cat.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/cat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cat.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/cat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cat

[f]파일을 출력하고 연결.
더 많은 정보: <https://www.gnu.org/software/coreutils/cat>.

- [f]파일의 내용을 `stdout`에 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 여러 [f]파일을 연결하여 출력 [f]파일로 저장:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 여러 [f]파일을 출력 [f]파일에 추가:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- `stdin`을 [f]파일로 작성:

`cat - > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 모든 출력 줄에 [n]번호 추가:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 비인쇄 및 공백 문자를 표시 (비ASCII의 경우 `M-` 접두사 사용):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
