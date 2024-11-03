---
layout: page
title: common/qmmp (한국어)
description: "Winamp 또는 XMMS와 유사한 인터페이스를 가진 오디오 플레이어."
content_hash: ed4825a17583919038c18fca34a0495889f17f49
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/qmmp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qmmp

Winamp 또는 XMMS와 유사한 인터페이스를 가진 오디오 플레이어.
같이 보기: `clementine`, `ncmpcpp`, `cmus`.
더 많은 정보: <https://qmmp.ylsoftware.com>.

- GUI 실행:

`qmmp`

- 현재 재생 중인 오디오 시작 또는 중지:

`qmmp --play-pause`

- 지정된 시간(초)만큼 앞으로 또는 뒤로 탐색:

`qmmp --seek-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fwd|bwd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간_초</span>

- 다음 오디오 파일 재생:

`qmmp --next`

- 이전 오디오 파일 재생:

`qmmp --previous`

- 현재 볼륨 표시:

`qmmp --volume-status`

- 현재 재생 중인 오디오의 볼륨을 5% 증가 또는 감소:

`qmmp --volume-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc|dec</span>
