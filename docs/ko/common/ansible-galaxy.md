---
layout: page
title: common/ansible-galaxy (한국어)
description: "수용 가능한 역할 생성 및 관리."
content_hash: 817f74ee4cd0c145b9bc6e8ffc5d5bb11ded1fb7
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible-galaxy.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ansible-galaxy

수용 가능한 역할 생성 및 관리.
더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- 역할 설치:

`ansible-galaxy install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름.역할_</span>

- 역할 제거:

`ansible-galaxy remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름.역할_이름</span>

- 설치된 역할 리스트:

`ansible-galaxy list`

- 주어진 역할에 대해 검색:

`ansible-galaxy search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할_이름</span>

- 새로운 역할 생성:

`ansible-galaxy init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할_이름</span>
