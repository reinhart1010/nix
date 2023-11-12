---
layout: page
title: common/blender (한국어)
description: "Blender 3D 컴퓨터 그래픽스 어플리케이션의 커맨드라인 인터페이스. 인자는 주어진 순서대로 실행."
content_hash: 662b3bdb4459feb1927d0a876b6649180f9a9f42
last_modified_at: 2023-11-12
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

- UI를 로드하지 않고 background에서 애니메이션의 모든 프레임을 렌더링.(출력은 `/tmp`에 저장):

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>`.blend -a`

- .blend 파일에 대한 경로 (`//`)에서 특정 이미지 명명 패턴을 사용하여 애니메이션 렌더링:

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>`.blend -o //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">render/frame_###.png</span>` -a`

- 기존 디렉토리에 저장된 단일 이미지로 애니메이션의 10번째 프레임 렌더링(절대 경로):

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>`.blend -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/출력_디렉토리/의/경로</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 기존 디렉토리에 저장된 JPEG 이미지로 애니메이션의 두번째 마지막 프레임 렌더링(상대 경로):

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>`.blend -o //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_디렉토리</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JPEG</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-2</span>

- 프레임 10에서 시작하여 프레임 500에서 끝나는 특정 장면의 애니메이션 렌더링:

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>`.blend -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">씬_이름</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` -a`

- Python 표현식을 전달하여 특정 해상도로 애니메이션 렌더링:

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>`.blend --python-expr '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import bpy; bpy.data.scenes[0].render.resolution_percentage = 25</span>`' -a`

- Python 콘솔을 사용하여 터미널에서 대화형 Blender 세션 시작(시작 후`import bpy` 수행):

`blender -b --python-console`
