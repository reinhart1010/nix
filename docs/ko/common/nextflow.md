---
layout: page
title: common/nextflow (한국어)
description: "계산 파이프라인 실행. 주로 생물정보학 워크플로우에 사용됩니다."
content_hash: 098a6a5ecc538a02363c8e57c50e26c999c472ef
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nextflow.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nextflow.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nextflow

계산 파이프라인 실행. 주로 생물정보학 워크플로우에 사용됩니다.
더 많은 정보: <https://www.nextflow.io>.

- 파이프라인 실행, 이전 실행의 캐시된 결과 사용:

`nextflow run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main.nf</span>` -resume`

- GitHub에서 원격 워크플로우의 특정 릴리스 실행:

`nextflow run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자/저장소</span>` -revision `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">릴리스_태그</span>

- 중간 파일을 위한 작업 디렉토리를 지정하고 실행 보고서 저장:

`nextflow run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">워크플로우</span>` -work-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` -with-report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">보고서.html</span>

- 현재 디렉토리에서 이전 실행의 세부 정보 표시:

`nextflow log`

- 특정 실행의 캐시 및 중간 파일 제거:

`nextflow clean -force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_이름</span>

- 다운로드된 모든 프로젝트 나열:

`nextflow list`

- Bitbucket에서 원격 워크플로우의 최신 버전 가져오기:

`nextflow pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자/저장소</span>` -hub bitbucket`

- Nextflow 업데이트:

`nextflow self-update`
