---
layout: page
title: linux/qm-guest-exec (한국어)
description: "게스트 에이전트를 통해 특정 명령 실행."
content_hash: 2612ba56abba5ca06ad2ec838090b7b19f7487ee
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/qm-guest-exec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qm-guest-exec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qm guest exec

게스트 에이전트를 통해 특정 명령 실행.
더 많은 정보: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- 게스트 에이전트를 통해 특정 명령 실행:

`qm guest exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

- 게스트 에이전트를 통해 비동기적으로 특정 명령 실행:

`qm guest exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>` --synchronous 0`

- 10초의 지정된 제한 시간으로 게스트 에이전트를 통해 특정 명령 실행:

`qm guest exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 게스트 에이전트를 통해 특정 명령 실행 및 STDIN에서 EOF까지 입력을 게스트 에이전트로 전달:

`qm guest exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상_머신_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>` --pass-stdin 1`
