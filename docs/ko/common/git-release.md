---
layout: page
title: common/git-release (한국어)
description: "릴리스를 위한 Git 태그 생성."
content_hash: 7a10920473f5809ac3d3533eabff75c162f9844d
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-release.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git release

릴리스를 위한 Git 태그 생성.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-release>.

- 릴리스 생성 및 푸시:

`git release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 서명된 릴리스 생성 및 푸시:

`git release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>` -s`

- 메시지와 함께 릴리스 생성 및 푸시:

`git release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`
