---
layout: page
title: common/croc (한국어)
description: "모든 네트워크를 통해 쉽고 안전하게 파일을 보내고 받을 수 있음."
content_hash: c661d66b850d17cd6a3644a8b265f75c723bf734
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/croc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/croc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># croc

모든 네트워크를 통해 쉽고 안전하게 파일을 보내고 받을 수 있음.
더 많은 정보: <https://github.com/schollz/croc>.

- 파일 또는 디렉터리 전송:

`croc send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 특정 암호를 사용하여 파일이나 디렉터리를 전송:

`croc send --code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 수신 시스템에서 파일 또는 디렉터리 수신:

`croc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>

- 맞춤형 릴레이를 통해 전송 및 연결:

`croc --relay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_to_relay</span>` send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 맞춤형 릴레이를 통해 수신 및 연결:

`croc --relay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_to_relay</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>

- 기본 포트에서 croc 릴레이를 호스팅:

`croc relay`

- croc 명령에 대한 매개변수 및 옵션 표시:

`croc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">send|relay</span>` --help`
