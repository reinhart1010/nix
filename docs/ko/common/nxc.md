---
layout: page
title: common/nxc (한국어)
description: "네트워크 서비스 열거 및 익스플로잇 도구."
content_hash: 46273f92e3a8efcd4f7854fc0941e9fbe35e0b1c
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/nxc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nxc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nxc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nxc

네트워크 서비스 열거 및 익스플로잇 도구.
`smb`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://www.netexec.wiki/>.

- 지정된 프로토콜에 대한 사용 가능한 모듈 [L]ist:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` -L`

- 지정된 모듈에 대한 사용 가능한 옵션 나열:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>` --options`

- 모듈에 대한 옵션 지정:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션_이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션_값</span>

- 지정된 프로토콜에 대한 사용 가능한 옵션 보기:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` --help`
