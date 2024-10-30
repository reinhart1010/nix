---
layout: page
title: common/dolt-config (한국어)
description: "로컬 (저장소별) 및 전역 (사용자별) Dolt 구성 변수 읽기 및 쓰기."
content_hash: f6ae422131749cb5afb9873f7a30e9cccfff92e0
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/dolt-config.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dolt-config.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dolt config

로컬 (저장소별) 및 전역 (사용자별) Dolt 구성 변수 읽기 및 쓰기.
더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-config>.

- 모든 로컬 및 글로벌 구성 옵션과 해당 값을 나열:

`dolt config --list`

- 로컬 또는 전역 구성 변수의 값을 표시:

`dolt config --get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 로컬 구성 변수의 값을 수정하여, 존재하지 않는 경우 생성:

`dolt config --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 전역 구성 변수의 값을 수정하여, 존재하지 않는 경우 생성:

`dolt config --global --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 로컬 구성 변수를 삭제:

`dolt config --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 전역 구성 변수를 삭제:

`dolt config --global --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
