---
layout: page
title: linux/firejail (한국어)
description: "Linux의 내장 기능을 사용하여 프로세스를 안전하게 컨테이너로 샌드박스화합니다."
content_hash: 5fdc9cb35f39a710ab27aa41e671470422a79530
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/firejail.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/firejail.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># firejail

Linux의 내장 기능을 사용하여 프로세스를 안전하게 컨테이너로 샌드박스화합니다.
더 많은 정보: <https://manned.org/firejail>.

- 데스크톱 환경에 firejail 통합:

`sudo firecfg`

- 제한된 Mozilla Firefox 열기:

`firejail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- 알려진 인터페이스와 주소에서 제한된 Apache 서버 시작:

`firejail --net=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` --ip=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.244</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/init.d/apache2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start</span>

- 실행 중인 샌드박스 나열:

`firejail --list`

- 실행 중인 샌드박스의 네트워크 활동 나열:

`firejail --netstats`

- 실행 중인 샌드박스 종료:

`firejail --shutdown=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7777</span>

- 인터넷 탐색을 위한 제한된 Firefox 세션 실행:

`firejail --seccomp --private --private-dev --private-tmp --protocol=inet firefox --new-instance --no-remote --safe-mode --private-window`

- 사용자 정의 호스트 파일 사용(`/etc/hosts` 파일 무시):

`firejail --hosts-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/myhosts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">curl http://mysite.arpa</span>
