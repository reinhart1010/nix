---
layout: page
title: common/zoxide (한국어)
description: "가장 자주 사용되는 디렉터리를 추적."
content_hash: 9d1d8c0d78f0e1d9f4f8a46a06f390ee4927b2fe
last_modified_at: 2024-11-02
related_topics:
  - title: Deutsch version
    url: /de/common/zoxide.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/zoxide.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zoxide.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zoxide

가장 자주 사용되는 디렉터리를 추적.
순위 알고리즘을 사용하여 가장 적합한 경로로 이동.
더 많은 정보: <https://github.com/ajeetdsouza/zoxide>.

- 이름에 "foo"가 포함된 가장 높은 순위의 디렉터리로 이동:

`zoxide query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 이름에 "foo"와 "bar"가 차례로 포함된 가장 높은 순위의 디렉터리로 이동:

`zoxide query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- 대화형 디렉터리 검색 시작 (`fzf` 필요):

`zoxide query --interactive`

- 디렉터리를 추가하거나 순위를 증가:

`zoxide add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- `zoxide` 데이터베이스에서 대화형으로 디렉터리 제거:

`zoxide remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --interactive`

- 명령 별칭 (`z`, `za`, `zi`, `zq`, `zr`)에 대한 쉘 구성 생성:

`zoxide init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|zsh</span>
