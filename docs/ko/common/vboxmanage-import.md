---
layout: page
title: common/vboxmanage-import (한국어)
description: "이전에 내보낸 가상 머신(VM)을 가져오기."
content_hash: 6d4966a5b38b03e596c50239d3c22b5dc5dc0674
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/vboxmanage-import.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-import.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-import

이전에 내보낸 가상 머신(VM)을 가져오기.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-import>.

- OVF 또는 OVA 파일에서 VM 가져오기:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ovf</span>

- 가져온 VM의 이름 설정:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ovf</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_이름</span>

- 가져온 VM의 구성 파일이 저장될 폴더 지정:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ovf</span>` --basefolder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- VirtualBox에 가져온 VM 등록:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ovf</span>` --register`

- 실제로 가져오지 않고 가져오기를 확인하는 드라이런 수행:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ovf</span>` --dry-run`

- 가져온 VM의 게스트 OS 유형 설정 (`VBoxManage list ostypes` 중 하나):

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ovf</span>` --ostype=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os유형</span>

- 가져온 VM의 메모리 크기 설정 (메가바이트 단위):

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ovf</span>` --memory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 가져온 VM의 CPU 개수 설정:

`VBoxManage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ovf</span>` --cpus=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
