---
layout: page
title: common/wireplumber (한국어)
description: "PipeWire를 위한 모듈식 세션/정책 관리자 및 PipeWire의 API를 감싸는 GObject 기반 고수준 라이브러리."
content_hash: 308908eb64f13769337c844371a5d454ea8fa987
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/wireplumber.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wireplumber.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wireplumber

PipeWire를 위한 모듈식 세션/정책 관리자 및 PipeWire의 API를 감싸는 GObject 기반 고수준 라이브러리.
같이 보기: `wpctl`, `pipewire`.
더 많은 정보: <https://pipewire.pages.freedesktop.org/wireplumber/>.

- 사용자 세션과 함께 WirePlumber를 즉시 시작 (systemd 시스템의 경우):

`systemctl --user --now enable wireplumber`

- `pipewire`가 시작된 후 WirePlumber 실행 (non-systemd 시스템의 경우):

`wireplumber`

- 다른 컨텍스트 구성 파일 지정:

`wireplumber --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 도움말 표시:

`wireplumber --help`

- 버전 표시:

`wireplumber --version`
