---
layout: page
title: linux/dpkg-deb (한국어)
description: "Debian 아카이브를 패키징, 압축 해제 및 정보 제공."
content_hash: 51b22e21e1c347aa0b695ed8894e6cae16586cac
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dpkg-deb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg-deb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dpkg-deb

Debian 아카이브를 패키징, 압축 해제 및 정보 제공.
더 많은 정보: <https://manned.org/dpkg-deb>.

- 패키지 정보 표시:

`dpkg-deb --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.deb</span>

- 패키지의 이름과 버전을 한 줄로 표시:

`dpkg-deb --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.deb</span>

- 패키지의 내용 나열:

`dpkg-deb --contents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.deb</span>

- 패키지의 내용을 디렉토리에 추출:

`dpkg-deb --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 지정된 디렉토리에서 패키지 생성:

`dpkg-deb --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
