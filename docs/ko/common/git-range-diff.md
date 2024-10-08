---
layout: page
title: common/git-range-diff (한국어)
description: "두 커밋 범위(예: 브랜치의 두 버전)를 비교."
content_hash: b02a203e8842b0c75c29b1e6ae1cbdbce298c04b
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-range-diff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git range-diff

두 커밋 범위(예: 브랜치의 두 버전)를 비교.
더 많은 정보: <https://git-scm.com/docs/git-range-diff>.

- 두 개별 커밋의 변경 사항을 비교:

`git range-diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_1</span>`^! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_2</span>`^!`

- 공통 조상으로부터 ours와 theirs의 변경 사항을 비교 (예: 인터랙티브 리베이스 후):

`git range-diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">theirs</span>`...`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ours</span>

- 두 커밋 범위의 변경 사항을 비교 (예: `base1`에서 `base2`로 리베이스하는 동안 충돌이 적절하게 해결되었는지 확인):

`git range-diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rev1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base2</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rev2</span>
