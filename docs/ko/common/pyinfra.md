---
layout: page
title: common/pyinfra (한국어)
description: "대규모 인프라를 자동화."
content_hash: 03e3654e2aab366958a126f903a67c418b1d6cb8
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pyinfra.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pyinfra.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pyinfra

대규모 인프라를 자동화.
더 많은 정보: <https://docs.pyinfra.com>.

- SSH를 통해 명령 실행:

`pyinfra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_IP_주소</span>` exec -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_및_인수</span>

- 대상 목록에 있는 서버에 배포 파일의 내용을 실행:

`pyinfra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목록.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/배포.py</span>

- 로컬에서 명령 실행:

`pyinfra @local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/배포.py</span>

- Docker를 통해 명령 실행:

`pyinfra @docker/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/배포.py</span>
