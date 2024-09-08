---
layout: page
title: common/ansible-vault (한국어)
description: "Ansible 프로젝트 내에서 값, 데이터 구조 및 파일을 암호화하고 해독."
content_hash: c57fda74b54c0e88efb8c219e041e2090699d058
last_modified_at: 2024-09-08
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-vault.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-vault.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-vault.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ansible-vault.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-vault

Ansible 프로젝트 내에서 값, 데이터 구조 및 파일을 암호화하고 해독.
더 많은 정보: <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.

- 비밀번호를 입력하라는 메시지가 표시된 새로운 암호화된 볼트 파일을 만듬:

`ansible-vault create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼트_파일</span>

- 볼트 키 파일을 사용하여, 암호화된 새 볼트 파일을 만듬:

`ansible-vault create --vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼트_파일</span>

- 선택적 비밀번호 파일을 사용하여, 기존 파일을 암호화:

`ansible-vault encrypt --vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼트_파일</span>

- Ansible의 암호화된 문자열 형식을 사용하여, 문자열을 암호화하고 대화형 프롬프트를 표시:

`ansible-vault encrypt_string`

- 암호 파일을 사용하여, 암호화된 파일을 해독하는 방법:

`ansible-vault view --vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼트_파일</span>

- 이미 암호화된 볼트 파일을 새 암호 파일로 다시 키 지정:

`ansible-vault rekey --vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예전_비밀번호_파일</span>` --new-vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_비밀번호_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼트_파일</span>
