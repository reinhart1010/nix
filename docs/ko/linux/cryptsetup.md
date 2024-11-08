---
layout: page
title: linux/cryptsetup (한국어)
description: "평문 `dm-crypt` 및 LUKS (Linux Unified Key Setup) 암호화 볼륨을 관리."
content_hash: 443f551264dc9ba4884feada8ee11881e730858d
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/cryptsetup.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/cryptsetup.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cryptsetup.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cryptsetup

평문 `dm-crypt` 및 LUKS (Linux Unified Key Setup) 암호화 볼륨을 관리.
`luksFormat`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://manned.org/cryptsetup>.

- 암호를 사용하여 LUKS 볼륨 초기화 (파티션의 모든 데이터를 덮어씁니다):

`cryptsetup luksFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- LUKS 볼륨을 열고 `/dev/mapper/mapping_name`에 복호화된 매핑 생성:

`cryptsetup open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매핑_이름</span>

- 매핑에 대한 정보 표시:

`cryptsetup status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매핑_이름</span>

- 기존 매핑 제거:

`cryptsetup close `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매핑_이름</span>

- LUKS 볼륨의 암호 변경:

`cryptsetup luksChangeKey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>
