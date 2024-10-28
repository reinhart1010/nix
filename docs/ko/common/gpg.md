---
layout: page
title: common/gpg (한국어)
description: "GNU Privacy Guard."
content_hash: daa343264ed8f879826fdd463c62f9b20f6a2944
last_modified_at: 2024-10-28
related_topics:
  - title: Deutsch version
    url: /de/common/gpg.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gpg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gpg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gpg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gpg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gpg

GNU Privacy Guard.
GNU Privacy Guard 2에 대해서는 `gpg2`를 참조. 대부분의 운영체제는 `gpg`를 `gpg2`에 심볼릭 링크를 설정함.
더 많은 정보: <https://gnupg.org>.

- GPG 공개 및 개인 키를 대화형으로 생성:

`gpg --full-generate-key`

- 암호화 없이 `doc.txt`에 서명 (`doc.txt.asc`에 출력을 기록):

`gpg --clearsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- alice@example.com 및 bob@example.com에 대해 `doc.txt`를 암호화하고 서명 (`doc.txt.gpg`로 출력):

`gpg --encrypt --sign --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>` --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bob@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- 비밀번호 문구만으로 `doc.txt`를 암호화 (`doc.txt.gpg`로 출력):

`gpg --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- `doc.txt.gpg` 복호화 (`stdout`으로 출력):

`gpg --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt.gpg</span>

- 공개 키 가져오기:

`gpg --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public.gpg</span>

- alice@example.com에 대한 공개 키 내보내기 (`stdout`으로 출력):

`gpg --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>

- alice@example.com의 개인 키 내보내기 (`stdout`으로 출력):

`gpg --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>
