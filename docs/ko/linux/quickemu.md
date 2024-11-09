---
layout: page
title: linux/quickemu (한국어)
description: "고도로 최적화된 데스크탑 가상 머신을 빠르게 구축하고 관리합니다."
content_hash: 5bf3bb665d18e7936560b2056fd911819ec6eb55
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/quickemu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/quickemu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># quickemu

고도로 최적화된 데스크탑 가상 머신을 빠르게 구축하고 관리합니다.
같이 보기: VM 설정 준비를 위한 `quickget`.
더 많은 정보: <https://github.com/quickemu-project/quickemu>.

- 구성 파일에서 가상 머신 생성 및 실행:

`quickemu --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.conf</span>

- 디스크/스냅샷에 변경 사항을 저장하지 않고 임시 파일에 변경 사항 기록:

`quickemu --status-quo --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.conf</span>

- 전체 화면 모드로 가상 머신 시작 (<Ctrl> + <Alt> + f로 종료) 및 디스플레이 백엔드 선택 (기본값은 `sdl`):

`quickemu --fullscreen --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdl|gtk|spice|spice-app|none</span>` --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.conf</span>

- 가상 오디오 장치를 에뮬레이트하고 데스크탑 바로 가기 생성:

`quickemu --sound-card `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">intel-hda|ac97|es1370|sb16|none</span>` --shortcut --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.conf</span>

- 스냅샷 생성:

`quickemu --snapshot create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>` --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.conf</span>

- 스냅샷 복원:

`quickemu --snapshot apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>` --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.conf</span>

- 스냅샷 삭제:

`quickemu --snapshot delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>` --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.conf</span>
