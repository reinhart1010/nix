---
layout: page
title: common/blender (한국어)
description: "Blender 3D 컴퓨터 그래픽스 어플리케이션의 커맨드라인 인터페이스. 인자는 주어진 순서대로 실행."
content_hash: 00d47f7d3a344bf22ec8a05749bf28a5c7a3b649
last_modified_at: 2024-01-15
related_topics:
  - title: English version
    url: /en/common/blender.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/blender.html
    icon: bi bi-globe
tldri18n_status: 2
---
# blender

Blender 3D 컴퓨터 그래픽스 어플리케이션의 커맨드라인 인터페이스. 인자는 주어진 순서대로 실행.
더 많은 정보: <https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html>.

- UI를 로드하지 않고 백그라운드에서 애니메이션의 모든 프레임을 렌더링(출력은 `/tmp`에 저장):

`blender --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`.blend --render-anim`

- .blend 파일에 대한 경로 (`//`)에서 특정 이미지 명명 패턴을 사용하여 애니메이션 렌더링:

`blender --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`.blend --render-output //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">render/frame_###.png</span>` --render-anim`

- 기존 디렉토리에 저장된 단일 이미지로 애니메이션의 10번째 프레임 렌더링(절대 경로):

`blender --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`.blend --render-output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/출력_디렉토리</span>` --render-frame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 기존 디렉토리에 저장된 JPEG 이미지로 애니메이션의 두번째 마지막 프레임 렌더링(상대 경로):

`blender --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`.blend --render-output //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_디렉토리</span>` --render-frame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JPEG</span>` --render-frame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-2</span>

- 프레임 10에서 시작하여 프레임 500에서 끝나는 특정 장면의 애니메이션 렌더링:

`blender --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`.blend --scene `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장면_이름</span>` --frame-start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --frame-end `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` --render-anim`

- Python 표현식을 전달하여 특정 해상도로 애니메이션 렌더링:

`blender --background `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`.blend --python-expr '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import bpy; bpy.data.scenes[0].render.resolution_percentage = 25</span>`' --render-anim`

- Python 콘솔을 사용하여 터미널에서 대화형 Blender 세션 시작(시작 후`import bpy` 수행):

`blender --background --python-console`
