---
layout: page
title: common/git-credential-store (한국어)
description: "디스크에 비밀번호를 저장하는 Git 도우미."
content_hash: e66793f35775482152c15bbf5fc61499778a0106
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/git-credential-store.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git credential-store

디스크에 비밀번호를 저장하는 Git 도우미.
더 많은 정보: <https://git-scm.com/docs/git-credential-store>.

- 특정 파일에 Git 자격 증명 저장:

`git config credential.helper 'store --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`'`
