---
layout: page
title: linux/btrfs (한국어)
description: "Linux용으로 설계된 카피 온 라이트(COW) 원칙 기반 파일 시스템."
content_hash: e7a0571fa3cdccd2a62b06867bc2e9a571db86c6
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/btrfs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/btrfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/btrfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># btrfs

Linux용으로 설계된 카피 온 라이트(COW) 원칙 기반 파일 시스템.
`device`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- 서브볼륨 생성:

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서브볼륨</span>

- 서브볼륨 목록 나열:

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- 공간 사용 정보 표시:

`sudo btrfs filesystem df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- 쿼터 활성화:

`sudo btrfs quota enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서브볼륨</span>

- 쿼터 표시:

`sudo btrfs qgroup show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서브볼륨</span>
