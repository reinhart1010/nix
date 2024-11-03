---
layout: page
title: common/vagrant (한국어)
description: "경량, 재생 가능, 휴대 가능한 개발 환경 관리 도구."
content_hash: e01504ae78a2f3173cbd1061caf414b53a7e72a4
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/vagrant.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vagrant.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vagrant

경량, 재생 가능, 휴대 가능한 개발 환경 관리 도구.
더 많은 정보: <https://www.vagrantup.com>.

- 현재 디렉토리에 기본 Vagrant 박스로 Vagrantfile 생성:

`vagrant init`

- HashiCorp Atlas에서 Ubuntu 20.04 (Focal Fossa) 박스로 Vagrantfile 생성:

`vagrant init ubuntu/focal64`

- Vagrant 환경 시작 및 프로비저닝:

`vagrant up`

- 머신 일시 중지:

`vagrant suspend`

- 머신 중지:

`vagrant halt`

- SSH를 통해 머신에 연결:

`vagrant ssh`

- 실행 중인 Vagrant 머신의 SSH 구성 파일 출력:

`vagrant ssh-config`

- 모든 로컬 박스 나열:

`vagrant box list`
