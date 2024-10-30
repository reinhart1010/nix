---
layout: page
title: common/dolt-merge (한국어)
description: "두 개 이상의 개발 이력을 함께 결합."
content_hash: 6e2ca9a2a277db5a5a3be53a97c12b6362619bdd
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/dolt-merge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dolt-merge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dolt merge

두 개 이상의 개발 이력을 함께 결합.
더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-merge>.

- 이름이 있는 커밋의 변경 사항을 현재 브랜치에 통합:

`dolt merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 커밋 기록을 업데이트하지 않고, 명명된 커밋의 변경 사항을 현재 브랜치에 통합:

`dolt merge --squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 병합이 빨리-감기로 해결되는 경우에도, 브랜치를 병합하고 병합 커밋을 생성:

`dolt merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 브랜치를 병합하고 특정 커밋 메시지가 포함된 병합 커밋을 생성:

`dolt merge --no-ff -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 현재 충돌 해결 프로세스를 중단:

`dolt merge --abort`
