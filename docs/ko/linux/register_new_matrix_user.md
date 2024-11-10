---
layout: page
title: linux/register_new_matrix_user (한국어)
description: "등록이 비활성화된 상태에서 홈 서버에 새 사용자 등록."
content_hash: 5f6188b5bdb0b67fc0673c8c77a97fd9a00abbf6
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/register_new_matrix_user.html
    icon: bi bi-globe
tldri18n_status: 2
---
# register_new_matrix_user

등록이 비활성화된 상태에서 홈 서버에 새 사용자 등록.
더 많은 정보: <https://manned.org/register_new_matrix_user>.

- 대화형으로 사용자 생성:

`register_new_matrix_user --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/홈서버.yaml</span>

- 대화형으로 관리자 사용자 생성:

`register_new_matrix_user --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/홈서버.yaml</span>` --admin`

- 비대화형으로 관리자 사용자 생성(권장하지 않음):

`register_new_matrix_user --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/홈서버.yaml</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --admin`
