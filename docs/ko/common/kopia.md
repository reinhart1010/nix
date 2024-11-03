---
layout: page
title: common/kopia (한국어)
description: "빠르고 안전한 오픈 소스 백업 도구."
content_hash: 1e0b0404bade20e30691968ca543ef84a1e91e2f
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/kopia.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/kopia.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kopia

빠르고 안전한 오픈 소스 백업 도구.
암호화, 압축, 중복 제거 및 증분 스냅샷을 지원합니다.
더 많은 정보: <https://kopia.io/docs/reference/command-line/>.

- 로컬 파일 시스템에 저장소 생성:

`kopia repository create filesystem --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로컬_저장소</span>

- Amazon S3에 저장소 생성:

`kopia repository create s3 --bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>` --access-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AWS_액세스_키_ID</span>` --secret-access-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AWS_비밀_액세스_키</span>

- 저장소에 연결:

`kopia repository connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_유형</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>

- 디렉터리의 스냅샷 생성:

`kopia snapshot create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 스냅샷 나열:

`kopia snapshot list`

- 특정 디렉터리에 스냅샷 복원:

`kopia snapshot restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표_폴더</span>

- 새 정책 생성:

`kopia policy set --global --keep-latest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유지할_스냅샷_수</span>` --compression `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축_알고리즘</span>

- 특정 파일 또는 폴더를 백업에서 제외:

`kopia policy set --global --add-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>
