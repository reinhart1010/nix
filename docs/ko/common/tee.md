---
layout: page
title: common/tee (한국어)
description: "`stdin`에서 읽고 `stdout` 및 파일(또는 명령어)로 쓰기."
content_hash: b440b62c7cc6a1c5eda52558282def4586cf393b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tee.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tee.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tee.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tee.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tee

`stdin`에서 읽고 `stdout` 및 파일(또는 명령어)로 쓰기.
더 많은 정보: <https://www.gnu.org/software/coreutils/tee>.

- `stdin`을 각 파일과 `stdout`으로 복사:

`echo "example" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 파일에 덧붙이기, 덮어쓰지 않음:

`echo "example" | tee -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`을 터미널에 출력하고, 다른 프로그램으로 파이프하여 추가 처리:

`echo "example" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xargs printf "[%s]"</span>

- "example"이라는 디렉터리 만들기, "example"의 문자 수 세기, "example"을 터미널에 쓰기:

`echo "example" | tee >(xargs mkdir) >(wc -c)`
