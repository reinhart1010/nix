---
layout: page
title: osx/diskutil-partitiondisk (한국어)
description: "디스크 및 볼륨 내 파티션을 관리하는 도구."
content_hash: adab3d012cce414757ed562845a8d8beb74ca14f
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/diskutil-partitiondisk.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/diskutil-partitiondisk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diskutil partitionDisk

디스크 및 볼륨 내 파티션을 관리하는 도구.
`diskutil`의 일부.
APM은 macOS에서만 지원되고, MBR은 DOS에 최적화되어 있으며, GPT는 대부분의 최신 시스템과 호환됩니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- APM/MBR/GPT 파티션 방식을 사용하여 볼륨을 다시 포맷하고 안의 모든 파티션을 삭제 (볼륨의 모든 데이터가 지워집니다):

`diskutil partitionDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/디스크_장치</span>` 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">APM|MBR|GPT</span>

- 볼륨을 다시 포맷한 후, 모든 여유 공간을 사용하는 특정 파일 시스템으로 단일 파티션 생성:

`diskutil partitionDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/디스크_장치</span>` 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">APM|MBR|GPT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_파일시스템</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_이름</span>

- 볼륨을 다시 포맷한 후, 특정 크기 이하로 단일 파티션 생성 (예: `16G`는 16GB, `50%`는 전체 볼륨 크기의 절반):

`diskutil partitionDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/디스크_장치</span>` 1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">APM|MBR|GPT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_파일시스템</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_크기</span>

- 볼륨을 다시 포맷한 후, 여러 파티션 생성:

`diskutil partitionDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/디스크_장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">APM|MBR|GPT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_파일시스템1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_이름1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_크기1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_파일시스템2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_이름2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_크기2</span>` ...`

- 파티션을 위한 모든 지원 파일 시스템 나열:

`diskutil listFilesystems`
