---
layout: page
title: common/b2-tools (한국어)
description: "Backblaze B2 Cloud Storage의 모든 기능에 쉽게 액세스할 수 있음."
content_hash: aadbd6e6825b500672328021737ba6fcf3dd374f
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/b2-tools.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/b2-tools.html
    icon: bi bi-globe
tldri18n_status: 2
---
# b2-tools

Backblaze B2 Cloud Storage의 모든 기능에 쉽게 액세스할 수 있음.
더 많은 정보: <https://www.backblaze.com/docs/cloud-storage-command-line-tools>.

- 귀하의 계정에 접속:

`b2 authorize_account `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_아이디</span>

- 게정의 기존 버킷을 나열:

`b2 list_buckets`

- 버킷을 생성하고, 버킷 이름과 액세스 유형 (예, allPublic 또는 allPrivate을 제공):

`b2 create_bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">allPublic|allPrivate</span>

- 파일 업로드, 파일, 버킷, 폴더를 선택:

`b2 upload_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폴더_이름</span>

- Backblaze B2 버킷 대상에 소스 디렉터리를 업로드:

`b2 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>

- 한 버킷에서 다른 버킷으로 파일을 복사:

`b2 copy-file-by-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지_버킷_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/b2_file</span>

- 버킷에 있는 파일을 표시:

`b2 ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>

- 패턴과 일치하는 "폴더" 또는 파일 집합을 제거:

`b2 rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더|pattern</span>
