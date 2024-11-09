---
layout: page
title: linux/run-mailcap (한국어)
description: "MailCap 프로그램 실행."
content_hash: c080faf5acd31d97ecb8c9851dd8bd2445a43f8d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/run-mailcap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/run-mailcap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># run-mailcap

MailCap 프로그램 실행.
mailcap 파일(또는 그 별칭)의 항목을 통해 프로그램을 실행하여 각 MIME 타입/파일을 주어진 작업으로 처리.
더 많은 정보: <https://manned.org/run-mailcap>.

- run-mailcap에서 작업 플래그를 사용하여 개별 작업/프로그램 실행:

`run-mailcap --action=ACTION [--option[=value]]`

- 간단한 사용법:

`run-mailcap --action=ACTION `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- 추가 정보를 켜기:

`run-mailcap --action=ACTION --debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- "copiousoutput" 지시문을 무시하고 출력을 `stdout`으로 전달:

`run-mailcap --action=ACTION --nopager `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- 실제로 실행하지 않고 발견된 명령을 표시:

`run-mailcap --action=ACTION --norun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>
