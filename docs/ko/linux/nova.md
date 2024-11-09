---
layout: page
title: linux/nova (한국어)
description: "컴퓨팅 인스턴스를 프로비저닝하는 방법을 제공하는 OpenStack 프로젝트."
content_hash: 2fd69040499d7f3a7b86a703341dd0ee5c0d80f8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/nova.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nova.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nova

컴퓨팅 인스턴스를 프로비저닝하는 방법을 제공하는 OpenStack 프로젝트.
더 많은 정보: <https://docs.openstack.org/nova/latest/>.

- 현재 테넌트의 VM 나열:

`nova list`

- 모든 테넌트의 VM 나열 (관리자 사용자만 가능):

`nova list --all-tenants`

- 특정 호스트에 VM 부팅:

`nova boot --nic net-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_ID</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_ID</span>` --flavor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플레이버</span>` --availability-zone nova:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM_이름</span>

- 서버 시작:

`nova start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>

- 서버 중지:

`nova stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>

- 특정 VM에 네트워크 인터페이스 연결:

`nova interface-attach --net-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>
