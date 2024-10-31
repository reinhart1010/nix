---
layout: page
title: common/glab-repo (한국어)
description: "GitLab 레포지토리 작업."
content_hash: cce938555ced90fe3b6af8e7caec30aa5b66cecc
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/glab-repo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# glab repo

GitLab 레포지토리 작업.
더 많은 정보: <https://glab.readthedocs.io/en/latest/repo/index.html#synopsis>.

- 새로운 저장소를 생성 (저장소 이름이 설정되지 않은 경우, 기본 이름은 현재 디렉터리의 이름이 됨):

`glab repo create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 레포지토리 복제:

`glab repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리</span>

- 레포지토리 포크 및 복제:

`glab repo fork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리</span>` --clone`

- 기본 웹 브라우저에서 레포지토리 보기:

`glab repo view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리</span>` --web`

- GitLab 인스턴스에서 일부 레포지토리를 검색:

`glab repo search -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>
