---
layout: page
title: osx/yabai (polski)
description: "Kafelkowy menedżer okien dla macOS oparty na partycjonowaniu przestrzeni binarnej."
content_hash: f29352af56063de2b9be7351c5b4a51e43e8f3ab
last_modified_at: 2024-05-06
related_topics:
  - title: English version
    url: /en/osx/yabai.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/yabai.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yabai

Kafelkowy menedżer okien dla macOS oparty na partycjonowaniu przestrzeni binarnej.
Więcej informacji: <https://github.com/koekeishiya/yabai/wiki>.

- Wyślij wiado[m]ość konfiguracyjną w celu ustawienia układu:

`yabai -m config layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bsp|stack|float</span>

- Ustaw odstęp między oknami w pt:

`yabai -m config window_gap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Włącz nieprzezroczystość:

`yabai -m config window_opacity on`

- Wyłącz cienie okien:

`yabai -m config window_shadow off`

- Włącz pasek stanu:

`yabai -m config status_bar on`
