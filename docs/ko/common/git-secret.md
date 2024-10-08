---
layout: page
title: common/git-secret (한국어)
description: "Git 리포지토리에 개인 데이터를 저장. Bash로 작성됨."
content_hash: 6ad658e158f25728dfb873068d89f3d4f351fd39
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-secret.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git secret

Git 리포지토리에 개인 데이터를 저장. Bash로 작성됨.
더 많은 정보: <https://github.com/sobolevn/git-secret>.

- 로컬 리포지토리에 `git-secret` 초기화:

`git secret init`

- 현재 Git 사용자의 이메일에 액세스 권한 부여:

`git secret tell -m`

- 이메일로 액세스 권한 부여:

`git secret tell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>

- 이메일로 액세스 권한 취소:

`git secret killperson `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>

- 비밀에 대한 액세스 권한이 있는 이메일 목록:

`git secret whoknows`

- 비밀 파일 등록:

`git secret add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 비밀 암호화:

`git secret hide`

- 비밀 파일 복호화:

`git secret reveal`
