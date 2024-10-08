---
layout: page
title: common/git-verify-tag (한국어)
description: "태그의 GPG 서명을 검증."
content_hash: f57a99fee31d770588cbbee3228fcda4d9492664
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-verify-tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git verify-tag

태그의 GPG 서명을 검증.
태그가 서명되지 않은 경우 오류가 발생합니다.
더 많은 정보: <https://git-scm.com/docs/git-verify-tag>.

- 태그의 GPG 서명 검증:

`git verify-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그1 선택적_태그2 ...</span>

- 태그의 GPG 서명을 검증하고 각 태그에 대한 세부 정보를 표시:

`git verify-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그1 선택적_태그2 ...</span>` --verbose`

- 태그의 GPG 서명을 검증하고 원시 세부 정보를 출력:

`git verify-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그1 선택적_태그2 ...</span>` --raw`
