---
layout: page
title: common/nxc-ssh (한국어)
description: "SSH 서버를 침투 테스트하고 익스플로잇."
content_hash: 6de415245eb9860b877313b89d2b35d4b667d008
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/nxc-ssh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nxc-ssh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nxc-ssh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nxc ssh

SSH 서버를 침투 테스트하고 익스플로잇.
같이 보기: `hydra`.
더 많은 정보: <https://www.netexec.wiki/ssh-protocol>.

- 지정된 대상에서 사용자 목록에 대해 특정 [p]비밀번호를 스프레이:

`nxc ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자명목록.txt</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 지정된 [u]사용자명 및 [p]비밀번호 목록의 모든 조합을 시도하여 유효한 자격 증명 검색:

`nxc ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자명목록.txt</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀번호목록.txt</span>

- 제공된 [p]비밀번호를 키의 암호로 사용하여, 지정된 개인 키로 인증:

`nxc ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.186.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자명목록.txt</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --key-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/id_rsa</span>

- 여러 대상에 대해 [u]사용자명과 [p]비밀번호의 조합을 시도:

`nxc ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.0/24</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 성공적인 로그인 후 `sudo` 권한 확인:

`nxc ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀번호목록.txt</span>` --sudo-check`
