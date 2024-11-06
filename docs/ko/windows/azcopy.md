---
layout: page
title: windows/azcopy (한국어)
description: "Azure 클라우드 스토리지 계정에 업로드하기 위한 파일 전송 도구."
content_hash: 3585dd7f45bb4c29f97605d95ccf9ae120dd174e
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/azcopy.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/azcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# azcopy

Azure 클라우드 스토리지 계정에 업로드하기 위한 파일 전송 도구.
더 많은 정보: <https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10>.

- Azure 테넌트에 로그인:

`azopy login`

- 로컬 파일 업로드:

`azcopy copy '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_파일</span>`' 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토리지_계정_이름</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">블롭_이름</span>`'`

- `.txt` 및 `.jpg` 확장자를 가진 파일 업로드:

`azcopy copy '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_폴더</span>`' 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토리지_계정_이름</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>`' --include-pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt;*.jpg</span>`'`

- 두 Azure 스토리지 계정 간에 컨테이너 직접 복사:

`azcopy copy 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_스토리지_계정_이름</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>`' 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지_스토리지_계정_이름</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>`'`

- 로컬 디렉터리와 동기화하고 소스에 더 이상 존재하지 않는 파일을 대상에서 삭제:

`azcopy sync '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_폴더</span>`' 'https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토리지_계정_이름</span>`.blob.core.windows.net/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>`' --recursive --delete-destination=true`

- 도움말 표시:

`azcopy --help`
