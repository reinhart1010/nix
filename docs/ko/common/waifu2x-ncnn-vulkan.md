---
layout: page
title: common/waifu2x-ncnn-vulkan (한국어)
description: "NCNN 신경망 프레임워크를 사용하여 만화/애니메이션 스타일 이미지의 해상도를 높이는 도구."
content_hash: 8eaf1905d5f58769a19aaa14341fd371f24bece3
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/waifu2x-ncnn-vulkan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# waifu2x-ncnn-vulkan

NCNN 신경망 프레임워크를 사용하여 만화/애니메이션 스타일 이미지의 해상도를 높이는 도구.
더 많은 정보: <https://github.com/nihui/waifu2x-ncnn-vulkan>.

- 이미지 해상도 높이기:

`waifu2x-ncnn-vulkan -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 사용자 정의 배율로 이미지 해상도 높이고 노이즈 제거:

`waifu2x-ncnn-vulkan -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|4|8|16|32</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1|0|1|2|3</span>

- 특정 형식으로 해상도 높인 이미지 저장:

`waifu2x-ncnn-vulkan -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jpg|png|webp</span>
