---
layout: page
title: common/aws-workmail (한국어)
description: "Amazon WorkMail을 관리."
content_hash: fd4b7668f745d7f5cffeed3c1612cfd53db6eb59
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-workmail.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws workmail

Amazon WorkMail을 관리.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/index.html>.

- 모든 WorkMail 조직을 나열:

`aws workmail list-organizations`

- 특정 조직의 모든 사용자를 나열:

`aws workmail list-users --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_아이디</span>

- 특정 조직에서 WorkMail 사용자를 생성:

`aws workmail create-user --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --display-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_아이디</span>

- 그룹/사용자를 WorkMail에 등록하고 활성화:

`aws workmail register-to-work-mail --entity-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">엔티티_아이디</span>` --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일</span>` --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_아이디</span>

- 특정 조직에 WorkMail 그룹을 생성:

`aws workmail create-group --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>` --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_아이디</span>

- 특정 그룹에 구성원을 연결:

`aws workmail associate-member-to-group --group-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_아이디</span>` --member-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">멤버_아이디</span>` --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_아이디</span>

- WorkMail에서 사용자/그룹 등록을 취소하고 비활성화:

`aws workmail deregister-from-work-mail --entity-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">엔티티_아이디</span>` --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_아이디</span>

- 조직에서 사용자 삭제:

`aws workmail delete-user --user-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_아이디</span>` --organization-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직_아이디</span>
