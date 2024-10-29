---
layout: page
title: common/vboxmanage-export (한국어)
description: "가상 머신을 가상 어플라이언스(ISO) 또는 클라우드 서비스로 내보내기."
content_hash: 18681bfdf0b5fbcc64e4cd4e65aeb52333c3ace4
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/vboxmanage-export.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-export.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-export

가상 머신을 가상 어플라이언스(ISO) 또는 클라우드 서비스로 내보내기.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-export>.

- 대상 OVA 파일 지정:

`VBoxManage export --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름.ova</span>

- OVF 0.9 레거시 모드로 내보내기:

`VBoxManage export --legacy09`

- OVF (0.9|1.0|2.0) 형식으로 내보내기:

`VBoxManage export --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ovf09|ovf10|ovf20</span>

- 내보낸 파일의 매니페스트 생성:

`VBoxManage export --manifest`

- VM 설명 지정:

`VBoxManage export --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_설명</span>`"`
