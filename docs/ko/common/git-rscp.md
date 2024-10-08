---
layout: page
title: common/git-rscp (한국어)
description: "Reverse `git scp` - 원격 저장소의 작업 디렉터리에서 현재 작업 트리로 파일을 복사."
content_hash: bdd6cde40706fa5f1bc757bb868512f9e7e714b5
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-rscp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rscp

Reverse `git scp` - 원격 저장소의 작업 디렉터리에서 현재 작업 트리로 파일을 복사.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-scp>.

- 원격에서 특정 파일 복사:

`git rscp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 원격에서 특정 디렉터리 복사:

`git rscp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
