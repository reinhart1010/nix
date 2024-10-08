---
layout: page
title: common/git-replace (한국어)
description: "객체를 대체하기 위한 참조를 생성, 목록화 및 삭제."
content_hash: 5c2799acd1d51c1fb63bc72217e374a93d0e7551
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-replace.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-replace.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-replace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git replace

객체를 대체하기 위한 참조를 생성, 목록화 및 삭제.
더 많은 정보: <https://git-scm.com/docs/git-replace>.

- 특정 커밋을 다른 커밋으로 대체하고, 다른 커밋은 변경하지 않음:

`git replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체_객체</span>

- 주어진 객체에 대한 기존 대체 참조 삭제:

`git replace --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체</span>

- 객체의 내용을 대화형으로 편집:

`git replace --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체</span>
