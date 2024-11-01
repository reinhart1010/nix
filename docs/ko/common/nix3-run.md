---
layout: page
title: common/nix3-run (한국어)
description: "Nix 플레이크에서 애플리케이션 실행."
content_hash: 49730f25158b2eed7dd06e13ee73c6d2cab99785
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/nix3-run.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nix3-run.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nix run

Nix 플레이크에서 애플리케이션 실행.
같이 보기: 플레이크에 대한 정보는 `nix3 flake`.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-run.html>.

- 현재 디렉토리의 플레이크에서 기본 애플리케이션 실행:

`nix run`

- nixpkgs에서 패키지 이름과 일치하는 명령 실행 (해당 패키지의 다른 명령을 원하면 `tldr nix3 shell` 참조):

`nix run nixpkgs#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 제공된 인수와 함께 명령 실행:

`nix run nixpkgs#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vim</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 원격 저장소에서 실행:

`nix run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포</span>

- 특정 태그, 리비전 또는 브랜치를 사용하여 원격 저장소에서 실행:

`nix run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">참조</span>

- 하위 디렉토리와 프로그램을 지정하여 원격 저장소에서 실행:

`nix run "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포</span>`?dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리_이름</span>`#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱</span>`"`

- GitHub 풀 리퀘스트의 플레이크 실행:

`nix run github:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포</span>`/pull/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>`/head`
