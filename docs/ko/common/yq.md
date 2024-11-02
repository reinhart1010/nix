---
layout: page
title: common/yq (한국어)
description: "가볍고 휴대 가능한 명령줄 YAML 프로세서."
content_hash: 398c82a8139677a9f8c56bbed7785970e16e46b7
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/yq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yq

가볍고 휴대 가능한 명령줄 YAML 프로세서.
더 많은 정보: <https://mikefarah.gitbook.io/yq/>.

- YAML 파일을 보기 좋게 출력 (v4+):

`yq eval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.yaml</span>

- YAML 파일을 보기 좋게 출력 (v3):

`yq read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.yaml</span>` --colors`

- 배열만 포함된 YAML 파일에서 첫 번째 요소 출력 (v4+):

`yq eval '.[0]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.yaml</span>

- 배열만 포함된 YAML 파일에서 첫 번째 요소 출력 (v3):

`yq read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.yaml</span>` '[0]'`

- 파일에서 키를 값으로 설정 (또는 덮어쓰기) (v4+):

`yq eval '.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"' --inplace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.yaml</span>

- 파일에서 키를 값으로 설정 (또는 덮어쓰기) (v3):

`yq write --inplace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.yaml</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`'`

- 두 파일을 병합하여 `stdout`에 출력 (v4+):

`yq eval-all 'select(filename == "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.yaml</span>`") * select(filename == "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.yaml</span>`")' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.yaml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.yaml</span>

- 두 파일을 병합하여 `stdout`에 출력 (v3):

`yq merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.yaml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.yaml</span>` --colors`
