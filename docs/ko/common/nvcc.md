---
layout: page
title: common/nvcc (한국어)
description: "NVIDIA CUDA 컴파일러 드라이버."
content_hash: 97460b8667887dbba2d6267790151c277b59ef0c
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/nvcc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvcc

NVIDIA CUDA 컴파일러 드라이버.
더 많은 정보: <https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc>.

- CUDA 프로그램 컴파일:

`nvcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.cu</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>

- 디버그 정보 생성:

`nvcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.cu</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>` --debug --device-debug`

- 다른 경로에서 라이브러리 포함:

`nvcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.cu</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/포함대상</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/라이브러리</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라이브러리_이름</span>

- 특정 GPU 아키텍처에 대한 컴퓨팅 능력 지정:

`nvcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.cu</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>` --generate-code arch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아키텍처_이름</span>`,code=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpu_코드_이름</span>
