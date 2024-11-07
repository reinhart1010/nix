---
layout: page
title: common/rkdeveloptool (한국어)
description: "Rockchip 기반 컴퓨터 장치의 부팅 펌웨어를 플래시, 덤프 및 관리."
content_hash: 17eaf5b91e2655e11d30520a2ae6b1697ab42357
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rkdeveloptool.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rkdeveloptool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rkdeveloptool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rkdeveloptool

Rockchip 기반 컴퓨터 장치의 부팅 펌웨어를 플래시, 덤프 및 관리.
USB를 통해 연결하기 전에 장치를 Maskrom/Bootrom 모드로 전환해야 합니다.
일부 하위 명령은 루트 권한으로 실행해야 할 수 있습니다.
더 많은 정보: <https://github.com/rockchip-linux/rkdeveloptool>.

- 연결된 모든 Rockchip 기반 플래시 장치 [l]ist:

`rkdeveloptool ld`

- 지정된 파일에서 [b]ootloader를 다운로드 및 설치하도록 장치를 [d]ownload 모드로 초기화:

`rkdeveloptool db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/부트로더.bin</span>

- 부트[l]oader 소프트웨어를 새 버전으로 [u]pdate:

`rkdeveloptool ul `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/부트로더.bin</span>

- GPT 형식의 플래시 파티션에 이미지를 작성하고 초기 저장소 섹터를 지정 (일반적으로 `0x0` 또는 `0`):

`rkdeveloptool wl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초기_섹터</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.img</span>

- 사용자 친화적인 이름으로 플래시 파티션에 쓰기:

`rkdeveloptool wlx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.img</span>

- [r]eset/재부팅 [d]evice, Maskrom/Bootrom 모드에서 나와 선택된 플래시 파티션으로 부팅:

`rkdeveloptool rd`
