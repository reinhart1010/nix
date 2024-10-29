---
layout: page
title: common/vboxmanage-extpack (한국어)
description: "Oracle VirtualBox용 확장팩 관리 도구."
content_hash: 1d30899145d4badcb3b0b68d17d4105c2756d8c1
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/vboxmanage-extpack.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-extpack.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-extpack

Oracle VirtualBox용 확장팩 관리 도구.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-extpack>.

- VirtualBox에 확장팩 설치 (참고: 새 버전을 설치하기 전에 기존 버전을 제거해야 함):

`VBoxManage extpack install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.vbox-extpack</span>

- 기존 VirtualBox 확장팩 버전 제거:

`VBoxManage extpack install --replace`

- VirtualBox에서 확장팩 제거:

`VBoxManage extpack uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장팩_이름</span>

- 대부분의 제거 거부를 건너뛰고 확장팩 제거:

`VBoxManage extpack uninstall --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장팩_이름</span>

- 확장팩이 남긴 임시 파일 및 디렉토리 정리:

`VBoxManage extpack cleanup`
