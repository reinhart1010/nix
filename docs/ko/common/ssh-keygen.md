---
layout: page
title: common/ssh-keygen (한국어)
description: "인증, 비밀번호 없는 로그인 및 기타 용도로 사용되는 SSH 키 생성."
content_hash: ef95211bddbb9f55ece49b1244ac2bc44877ba43
last_modified_at: 2024-11-01
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-keygen.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh-keygen.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-keygen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-keygen.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ssh-keygen.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ssh-keygen

인증, 비밀번호 없는 로그인 및 기타 용도로 사용되는 SSH 키 생성.
더 많은 정보: <https://man.openbsd.org/ssh-keygen>.

- 대화식으로 키 생성:

`ssh-keygen`

- 32 키 유도 함수 라운드로 ed25519 키를 생성하고 특정 파일에 키 저장:

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ed25519</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">32</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/파일_이름</span>

- 이메일을 주석으로 하는 4096비트 RSA 키 생성:

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -C "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주석|이메일</span>`"`

- known_hosts 파일에서 호스트의 키 제거 (알려진 호스트가 새 키를 가지는 경우 유용):

`ssh-keygen -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- MD5 Hex로 키의 지문 검색:

`ssh-keygen -l -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md5</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/파일_이름</span>

- 키의 비밀번호 변경:

`ssh-keygen -p -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/파일_이름</span>

- 키 형식 변경 (예: OPENSSH 형식에서 PEM으로), 파일은 제자리에서 다시 작성됨:

`ssh-keygen -p -N "" -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PEM</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/OpenSSH_개인_키</span>

- 비밀 키에서 공개 키 추출:

`ssh-keygen -y -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/OpenSSH_개인_키</span>
