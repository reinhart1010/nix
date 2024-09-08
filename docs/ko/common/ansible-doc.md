---
layout: page
title: common/ansible-doc (한국어)
description: "Ansible 라이브러리에 설치된 모듈에 대한 정보를 표시."
content_hash: 976f20f0d25afe4bf86d938d84fc8010f3e9ca37
last_modified_at: 2024-09-08
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-doc.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-doc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-doc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-doc.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ansible-doc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-doc

Ansible 라이브러리에 설치된 모듈에 대한 정보를 표시.
플러그인과 간단한 설명의 정리된 목록을 표시.
더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- 사용 가능한 작업 플러그인(모듈) 목록:

`ansible-doc --list`

- 특정 유형의 사용 가능한 플러그인을 나열:

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">become|cache|callback|cliconf|connection|...</span>` --list`

- 특정 작업 플러그인(모듈)에 대한 정보 표시:

`ansible-doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin_name</span>

- 특정 유형의 플러그인에 대한 정보 표시:

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">become|cache|callback|cliconf|connection|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인_이름</span>

- 액션 플러그인(모듈)에 대한 플레이북 스니펫 표시:

`ansible-doc --snippet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인_이름</span>

- 액션 플러그인(모듈)에 대한 정보를 JSON으로 표시:

`ansible-doc --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인_이름</span>
