---
layout: page
title: common/ansible-playbook (한국어)
description: "SSH를 통해 원격 머신에서 playbook에 정의된 작업 실행."
content_hash: 5ee8170f179be8ab8febc3c44626ec93770c4331
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-playbook.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-playbook.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-playbook.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible-playbook.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible-playbook.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ansible-playbook

SSH를 통해 원격 머신에서 playbook에 정의된 작업 실행.
더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- playbook에서 작업 실행:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- 사용자 정의 호스트 인벤토리를 포함한 playbook에서 작업 실행:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인벤토리_파일</span>

- 명령어 라인을 통해 정의된 추가 변수를 사용하여 playbook에서 작업 실행:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값2</span>`"`

- json 파일에 정의된 추가 변수를 사용하여 playbook에서 작업 실행:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -e "@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수.json</span>`"`
