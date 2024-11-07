---
layout: page
title: common/molecule (한국어)
description: "Molecule은 Ansible 역할 테스트를 돕습니다."
content_hash: 856f87230454e76b6dfdc6b2ffea21f7647473c1
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/molecule.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/molecule.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># molecule

Molecule은 Ansible 역할 테스트를 돕습니다.
더 많은 정보: <https://molecule.readthedocs.io>.

- 새 Ansible 역할 생성:

`molecule init role --role-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할_이름</span>

- 테스트 실행:

`molecule test`

- 인스턴스 시작:

`molecule create`

- 인스턴스 구성:

`molecule converge`

- 인스턴스의 시나리오 나열:

`molecule matrix converge`

- 인스턴스에 로그인:

`molecule login`
