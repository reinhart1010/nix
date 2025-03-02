---
layout: page
title: linux/pw-loopback (한국어)
description: "PipeWire에서 루프백 장치를 생성."
content_hash: 25da8ac617598eb4805a0238326dc22d9e23afcf
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/pw-loopback.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-loopback.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-loopback.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-loopback

PipeWire에서 루프백 장치를 생성.
더 많은 정보: <https://docs.pipewire.org/page_man_pw-loopback_1.html>.

- 기본 루프백 동작으로 루프백 장치 생성:

`pw-loopback`

- 스피커에 자동으로 연결되는 루프백 장치 생성:

`pw-loopback -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[FL FR]</span>`' --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Sink</span>`'`

- 마이크에 자동으로 연결되는 루프백 장치 생성:

`pw-loopback -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[FL FR]</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Source</span>`'`

- 자동으로 아무것에도 연결되지 않는 더미 루프백 장치 생성:

`pw-loopback -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[FL FR]</span>`' --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Sink</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Source</span>`'`

- 스피커에 자동으로 연결되고 싱크와 소스 간 좌우 채널을 교환하는 루프백 장치 생성:

`pw-loopback --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Sink audio.position=[FL FR]</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">audio.position=[FR FL]</span>`'`

- 마이크에 자동으로 연결되고 싱크와 소스 간 좌우 채널을 교환하는 루프백 장치 생성:

`pw-loopback --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">audio.position=[FR FL]</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Source audio.position=[FL FR]</span>`'`
