---
layout: page
title: common/crane-push (한국어)
description: "로컬 이미지 콘텐츠를 원격 레지스트리로 푸시."
content_hash: 16b04c984180774ae5577e77152632b4e244f1f5
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/crane-push.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane push

로컬 이미지 콘텐츠를 원격 레지스트리로 푸시.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_push.md>.

- 로컬 이미지 콘텐츠를 원격 레지스트리로 푸시:

`crane push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tarball</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>

- 게시된 이미지 참조 목록이 있는 파일 경로:

`crane push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tarball</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` --image-refs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름</span>

- 이미지 모음을 단일 인덱스로 푸시 (경로에 여러 이미지가 있는 경우 필수):

`crane push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tarball</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` --index`

- 도움말 표시:

`crane push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
