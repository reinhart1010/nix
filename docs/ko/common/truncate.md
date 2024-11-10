---
layout: page
title: common/truncate (한국어)
description: "파일의 크기를 지정된 크기로 줄이거나 늘립니다."
content_hash: 258e07e9ddc450800bf158ee9c2cfc9d2ced71ae
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/truncate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/truncate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# truncate

파일의 크기를 지정된 크기로 줄이거나 늘립니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/truncate>.

- 기존 파일의 크기를 10GB로 설정하거나, 지정된 크기로 새 파일 생성:

`truncate --size 10G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 크기를 50MiB 늘리고, 구멍으로 채우기 (0바이트로 읽힘):

`truncate --size +50M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 끝에서 데이터를 제거하여 2GiB 줄이기:

`truncate --size -2G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 내용 비우기:

`truncate --size 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 내용 비우기, 파일이 존재하지 않으면 생성하지 않기:

`truncate --no-create --size 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
