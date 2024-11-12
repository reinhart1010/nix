---
layout: page
title: linux/gbp (한국어)
description: "Git을 사용하여 Debian 패키지 빌드 시스템과 통합하는 시스템."
content_hash: 80afc557d6131e18f8813478e5285f5b0715266c
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/gbp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gbp

Git을 사용하여 Debian 패키지 빌드 시스템과 통합하는 시스템.
더 많은 정보: <https://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html>.

- 기존 Debian 패키지를 gbp로 변환:

`gbp import-dsc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.dsc</span>

- 현재 디렉토리에서 기본 빌더(`debuild`)를 사용하여 패키지 빌드:

`gbp buildpackage -jauto -us -uc`

- Debian Bullseye용 `pbuilder` 환경에서 패키지 빌드:

`DIST=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bullseye</span>` ARCH=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">amd64</span>` gbp buildpackage -jauto -us -uc --git-builder=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git-pbuilder</span>

- `.changes` 파일에서 패키지를 소스 전용 업로드로 지정 (참조: <https://wiki.debian.org/SourceOnlyUpload>):

`gbp buildpackage -jauto -us -uc --changes-options=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-S</span>

- 새로운 업스트림 릴리스 가져오기:

`gbp import-orig --pristine-tar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.tar.gz</span>
