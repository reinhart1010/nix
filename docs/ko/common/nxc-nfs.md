---
layout: page
title: common/nxc-nfs (한국어)
description: "NFS 서버에 대한 펜테스트 및 익스플로잇 도구. 현재는 익명 모드만 지원."
content_hash: 76caafe2c9d9c27002f50ec26a0c259dc68aa251
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/nxc-nfs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nxc-nfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nxc nfs

NFS 서버에 대한 펜테스트 및 익스플로잇 도구. 현재는 익명 모드만 지원.
더 많은 정보: <https://www.netexec.wiki/nfs-protocol>.

- 원격 NFS 서버의 버전 감지:

`nxc nfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.0/24</span>

- 사용 가능한 NFS 공유 목록 나열:

`nxc nfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` --shares`

- 노출된 공유를 지정된 깊이까지 재귀적으로 열거:

`nxc nfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` --enum-shares `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 지정된 원격 파일 다운로드:

`nxc nfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` --get-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원격_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로컬_파일</span>

- 지정된 로컬 파일을 원격 공유에 업로드:

`nxc nfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` --put-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로컬_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원격_파일</span>
