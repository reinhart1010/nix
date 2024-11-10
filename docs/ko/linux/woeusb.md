---
layout: page
title: linux/woeusb (한국어)
description: "Windows 미디어 생성 도구."
content_hash: fb68c4ace688adcd58ec0dbb2fc8ecde5c55bc27
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/woeusb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# woeusb

Windows 미디어 생성 도구.
더 많은 정보: <https://github.com/WoeUSB/WoeUSB>.

- USB를 포맷하고 부팅 가능한 Windows 설치 드라이브 생성:

`woeusb --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/windows.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- USB 저장 장치의 기존 파티션에 Windows 파일을 복사하고 부팅 가능하게 만들기 (현재 데이터 삭제 없이):

`woeusb --partition `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/windows.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
