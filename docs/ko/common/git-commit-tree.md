---
layout: page
title: common/git-commit-tree (한국어)
description: "Git의 내부 동작을 직접 다루는 명령어로, 커밋 객체를 직접 생성합니다."
content_hash: 50a86f7db7efd61a4344304b3ceadc42a3df3be4
last_modified_at: 2024-08-23
related_topics:
  - title: English version
    url: /en/common/git-commit-tree.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit-tree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit-tree.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit-tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit-tree

Git의 내부 동작을 직접 다루는 명령어로, 커밋 객체를 직접 생성합니다.
참조: `git commit`.
더 많은 정보: <https://git-scm.com/docs/git-commit-tree>.

- 지정된 메시지로 커밋 객체 생성:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- 지정된 파일의 내용을 커밋 메시지로 사용하여 커밋 객체 생성 (`stdin`의 경우 `-` 사용):

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- GPG 키로 인증된 커밋 객체 생성:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" --gpg-sign`

- 지정된 부모 커밋 객체를 가진 커밋 객체 생성:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parent_commit_sha</span>
