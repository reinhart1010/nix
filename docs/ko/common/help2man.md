---
layout: page
title: common/help2man (한국어)
description: "실행 파일의 `--help` 및 `--version` 출력에서 간단한 매뉴얼 페이지 생성."
content_hash: c500e07041918e5bb53db760b84d48c5fe355aea
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/help2man.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/help2man.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># help2man

실행 파일의 `--help` 및 `--version` 출력에서 간단한 매뉴얼 페이지 생성.
더 많은 정보: <https://www.gnu.org/software/help2man>.

- 실행 파일에 대한 매뉴얼 페이지를 생성:

`help2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행파일</span>

- man 페이지에서 "이름" 단락을 지정:

`help2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행파일</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- man 페이지의 섹션을 지정 (기본값은 1):

`help2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행파일</span>` --section `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">섹션</span>

- `stdout` 대신 파일로 출력:

`help2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행파일</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 도움말 표시:

`help2man --help`
