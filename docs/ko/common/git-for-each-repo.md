---
layout: page
title: common/git-for-each-repo (한국어)
description: "여러 저장소에서 Git 명령을 실행."
content_hash: b6bb29822a8e8837087f74889458be4101993f22
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-for-each-repo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git for-each-repo

여러 저장소에서 Git 명령을 실행.
참고: 이 명령은 실험적이며 변경될 수 있습니다.
더 많은 정보: <https://git-scm.com/docs/git-for-each-repo>.

- `maintenance.repo` 사용자 구성 변수에 저장된 목록의 각 저장소에서 유지 관리를 실행:

`git for-each-repo --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maintenance.repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maintenance run</span>

- 글로벌 구성 변수에 나열된 각 저장소에서 `git pull` 실행:

`git for-each-repo --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global_configuration_variable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pull</span>
