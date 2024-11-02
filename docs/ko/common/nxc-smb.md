---
layout: page
title: common/nxc-smb (한국어)
description: "SMB 서버를 침투 테스트하고 익스플로잇."
content_hash: 3a6a145b8661705e6e070c75ce7e40c1f53ba328
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/nxc-smb.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nxc-smb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nxc-smb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nxc smb

SMB 서버를 침투 테스트하고 익스플로잇.
더 많은 정보: <https://www.netexec.wiki/smb-protocol>.

- 지정된 [u]사용자명 및 [p]비밀번호 목록의 모든 조합을 시도하여 유효한 도메인 자격 증명 검색:

`nxc smb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자명목록.txt</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀번호목록.txt</span>

- 도메인 계정 대신 로컬 계정에 대한 유효한 자격 증명 검색:

`nxc smb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자명목록.txt</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀번호목록.txt</span>` --local-auth`

- 대상 호스트에서 SMB 공유 및 지정된 사용자의 액세스 권한 열거:

`nxc smb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.0/24</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --shares`

- 패스-더-해시 인증을 통해 대상 호스트의 네트워크 인터페이스 열거:

`nxc smb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.30-45</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NTLM_해시</span>` --interfaces`

- 대상 호스트에서 일반적인 취약점 스캔:

`nxc smb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/target_list.txt</span>` -u '' -p '' -M zerologon -M petitpotam`

- 대상 호스트에서 명령 실행 시도:

`nxc smb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
