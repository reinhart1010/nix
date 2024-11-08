---
layout: page
title: common/lychee (한국어)
description: "깨진 URL을 찾기 위한 도구."
content_hash: 09a2730531056d2c2a4b796be01be64c46531cd9
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lychee.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lychee

깨진 URL을 찾기 위한 도구.
더 많은 정보: <https://lychee.cli.rs/usage/cli/>.

- 웹사이트에서 깨진 링크 스캔:

`lychee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 오류 유형의 세부 분류 표시:

`lychee --format detailed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- DDOS 보호를 방지하기 위해 연결 수 제한:

`lychee --max-concurrency `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">links.txt</span>

- 디렉터리 구조 내 파일에서 깨진 URL 확인:

`grep -r "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>`" | lychee -`

- 도움말 표시:

`lychee --help`
