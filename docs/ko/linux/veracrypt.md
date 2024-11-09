---
layout: page
title: linux/veracrypt (한국어)
description: "무료 및 오픈 소스 디스크 암호화 소프트웨어."
content_hash: 0c8107a5d2e41f465c915c4aac558bd56f0b6a99
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/veracrypt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/veracrypt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># veracrypt

무료 및 오픈 소스 디스크 암호화 소프트웨어.
더 많은 정보: <https://www.veracrypt.fr/code/VeraCrypt/plain/doc/html/Documentation.html>.

- 텍스트 사용자 인터페이스를 통해 새 볼륨을 생성하고 `/dev/urandom`을 무작위 데이터의 소스로 사용:

`veracrypt --text --create --random-source=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/urandom</span>

- 텍스트 사용자 인터페이스를 통해 볼륨을 상호작용적으로 복호화하고 디렉토리에 마운트:

`veracrypt --text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/볼륨</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- 키 파일을 사용하여 파티션을 복호화하고 디렉토리에 마운트:

`veracrypt --keyfiles=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- 마운트된 디렉토리에서 볼륨 마운트 해제:

`veracrypt --dismount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트된_포인트</span>
