---
layout: page
title: common/git-cvsexportcommit (한국어)
description: "단일 `Git` 커밋을 CVS 체크아웃으로 내보내기."
content_hash: 34eb25ac98f152d6eb6c5f9dba25ccd9f159f82c
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-cvsexportcommit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cvsexportcommit

단일 `Git` 커밋을 CVS 체크아웃으로 내보내기.
더 많은 정보: <https://git-scm.com/docs/git-cvsexportcommit>.

- 특정 패치를 CVS에 병합:

`git cvsexportcommit -v -c -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_cvs_체크아웃</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_sha1</span>
