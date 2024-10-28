---
layout: page
title: common/gpg2 (한국어)
description: "GNU Privacy Guard 2."
content_hash: 217030a954c44dc1abc93a8836da7b253bd7e1c7
last_modified_at: 2024-10-28
related_topics:
  - title: Deutsch version
    url: /de/common/gpg2.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gpg2.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gpg2.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gpg2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gpg2

GNU Privacy Guard 2.
GNU Privacy Guard 1에 대해서는 `gpg`를 참조.
더 많은 정보: <https://docs.releng.linuxfoundation.org/en/latest/gpg.html>.

- 가져온 키 목록 나열:

`gpg2 --list-keys`

- 지정된 수신자에 대해 지정된 파일을 암호화하고, `.gpg`가 추가된 새로운 파일에 출력을 작성:

`gpg2 --encrypt --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/문서.txt</span>

- 암호만 사용하여 지정된 파일을 암호화하고, `.gpg`가 추가된 새로운 파일에 출력을 작성:

`gpg2 --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/문서.txt</span>

- 지정된 파일의 암호를 복호화하고, 결과를 `stdout`에 기록:

`gpg2 --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/문서.txt.gpg</span>

- 공개 키 가져오기:

`gpg2 --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/공개_키.gpg</span>

- 지정된 이메일 주소의 공개 키를 `stdout`으로 내보내기 :

`gpg2 --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>

- 지정된 이메일 주소가 포함된 개인 키를 `stdout`으로 내보내기:

`gpg2 --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>
