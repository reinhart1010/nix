---
layout: page
title: common/colordiff (한국어)
description: "동일한 출력을 생성하지만, 구문 강조가 잘 되어있는 `diff` 래퍼입니다."
content_hash: 69c9a3d6bb9ad7e4db7408769dec584a7d58f3de
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/colordiff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/colordiff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/colordiff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># colordiff

동일한 출력을 생성하지만, 구문 강조가 잘 되어있는 `diff` 래퍼입니다.
색깔 구성표를 사용자 정의할 수 있음.
더 많은 정보: <https://github.com/kimmel/colordiff>.

- 파일 비교:

`colordiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>

- 두 개의 열로 출력:

`colordiff -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>

- 파일 내용의 대소문자 차이를 무시:

`colordiff -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>

- 두 파일이 동일한 경우에 보고:

`colordiff -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>

- 공백을 무시:

`colordiff -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>
