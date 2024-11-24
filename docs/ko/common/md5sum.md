---
layout: page
title: common/md5sum (한국어)
description: "MD5 암호화 체크섬 계산."
content_hash: 0d6f53e2e9e9b25903f825ecc28961962a13f828
last_modified_at: 2024-11-24
related_topics:
  - title: English version
    url: /en/common/md5sum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/md5sum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/md5sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/md5sum.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/md5sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># md5sum

MD5 암호화 체크섬 계산.
더 많은 정보: <https://www.gnu.org/software/coreutils/md5sum>.

- 하나 이상의 파일에 대한 MD5 체크섬 계산:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- MD5 체크섬 목록을 파일에 계산하고 저장:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.md5</span>

- `stdin`에서 MD5 체크섬 계산:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | md5sum`

- MD5 합 및 파일 이름이 포함된 파일을 읽고 모든 파일이 일치하는지 확인:

`md5sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.md5</span>

- 누락된 파일이나 확인 실패 시 메시지만 표시:

`md5sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.md5</span>

- 누락된 파일은 무시하고 확인 실패 시 메시지만 표시:

`md5sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.md5</span>
