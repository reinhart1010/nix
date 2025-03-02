---
layout: page
title: linux/pw-loopback (português (Brasil))
description: "Ferramenta para Cria dispositivos de loopback no PipeWire."
content_hash: f0c0699833d6a5d2c1e1a6d17ef432c4f6677acd
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/pw-loopback.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pw-loopback.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-loopback.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-loopback

Ferramenta para Cria dispositivos de loopback no PipeWire.
Mais informações: <https://docs.pipewire.org/page_man_pw-loopback_1.html>.

- Cria um dispositivo de loopback com o comportamento padrão de loopback:

`pw-loopback`

- Cria um dispositivo de loopback que se conecta automaticamente aos alto-falantes:

`pw-loopback -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[FL FR]</span>`' --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Sink</span>`'`

- Cria um dispositivo de loopback que se conecta automaticamente ao microfone:

`pw-loopback -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[FL FR]</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Source</span>`'`

- Cria um dispositivo fictício que não se conecta automaticamente a nada:

`pw-loopback -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[FL FR]</span>`' --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Sink</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Source</span>`'`

- Cria um dispositivo de loopback que se conecta automaticamente aos alto-falantes e troca os canais esquerdo e direito entre o dispositivo de entrada e o de saída:

`pw-loopback --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Sink audio.position=[FL FR]</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">audio.position=[FR FL]</span>`'`

- Cria um dispositivo de loopback que se conecta automaticamente ao microfone e troca os canais esquerdo e direito entre o dispositivo de entrada e o de saída:

`pw-loopback --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">audio.position=[FR FL]</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Source audio.position=[FL FR]</span>`'`
