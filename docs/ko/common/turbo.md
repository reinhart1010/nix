---
layout: page
title: common/turbo (한국어)
description: "JavaScript 및 TypeScript 코드베이스를 위한 고성능 빌드 시스템."
content_hash: 0c57e8aa012c75cb0018d2cd0548b5b3bef5248b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/turbo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/turbo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># turbo

JavaScript 및 TypeScript 코드베이스를 위한 고성능 빌드 시스템.
같이 보기: `nx`.
더 많은 정보: <https://turborepo.org/docs/reference/command-line-reference>.

- 기본 웹 브라우저를 사용하여 Vercel 계정으로 로그인:

`turbo login`

- 현재 디렉토리를 Vercel 조직에 연결하고 원격 캐싱 활성화:

`turbo link`

- 현재 프로젝트 빌드:

`turbo run build`

- 동시성 없이 작업 실행:

`turbo run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>` --concurrency=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 캐시된 아티팩트를 무시하고 모든 작업을 강제로 다시 실행:

`turbo run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>` --force`

- 패키지 전반에 걸쳐 병렬로 작업 실행:

`turbo run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>` --parallel --no-cache`

- 현재 디렉토리를 Vercel 조직에서 연결 해제하고 원격 캐싱 비활성화:

`turbo unlink`

- 특정 작업 실행의 Dot 그래프 생성 (출력 파일 형식은 파일 이름으로 제어 가능):

`turbo run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>` --graph=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.html|jpg|json|pdf|png|svg</span>
