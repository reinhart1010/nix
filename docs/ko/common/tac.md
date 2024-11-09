---
layout: page
title: common/tac (한국어)
description: "파일을 역순으로 표시하고 연결."
content_hash: 115e6f73172ba577f9236dceb771eed79e195f89
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tac.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/tac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tac.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tac.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tac

파일을 역순으로 표시하고 연결.
같이 보기: `cat`.
더 많은 정보: <https://www.gnu.org/software/coreutils/tac>.

- 특정 파일들을 역순으로 연결:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- `stdin`을 역순으로 표시:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 경로/대상/파일</span>` | tac`

- 특정 [s]eparator 사용:

`tac -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구분자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 [r]egex를 [s]eparator로 사용:

`tac -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구분자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 각 파일 앞에 구분자 [b]efore 사용:

`tac -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>
