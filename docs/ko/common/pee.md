---
layout: page
title: common/pee (한국어)
description: "`stdin`을 파이프로 전달하는 도구."
content_hash: 0626c394add7585cf635490e9d1a8f90f6884a0f
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pee.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pee.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pee

`stdin`을 파이프로 전달하는 도구.
같이 보기: `tee`.
더 많은 정보: <https://joeyh.name/code/moreutils/>.

- 각 명령을 실행하고, 각 명령에 `stdin`의 별도 복사본 제공:

`pee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령1 명령2 ...</span>

- `stdin`의 복사본을 `stdout`에 쓰기 (`tee`처럼 동작):

`pee cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령1 명령2 ...</span>

- SIGPIPE 및 쓰기 오류 발생 시 즉시 종료:

`pee --no-ignore-sigpipe --no-ignore-write-errors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령1 명령2 ...</span>
