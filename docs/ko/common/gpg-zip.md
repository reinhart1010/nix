---
layout: page
title: common/gpg-zip (한국어)
description: "GPG를 사용하여 아카이브의 파일과 디렉터리를 암호화."
content_hash: 9b3c83764d779c1ba411d0cfbf26d6f739792f10
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/gpg-zip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gpg-zip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpg-zip

GPG를 사용하여 아카이브의 파일과 디렉터리를 암호화.
더 많은 정보: <https://www.gnupg.org/documentation/manuals/gnupg/gpg_002dzip.html>.

- 비밀번호 문구를 사용하여 디렉터리를 `archive.gpg`로 암호화:

`gpg-zip --symmetric --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.gpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- `아카이브.gpg`를 같은 이름의 디렉터리로 복호화:

`gpg-zip --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.gpg</span>

- 암호화된 `아카이브.gpg`의 내용을 나열:

`gpg-zip --list-archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.gpg</span>
