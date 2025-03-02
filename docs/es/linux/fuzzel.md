---
layout: page
title: linux/fuzzel (español)
description: "Un lanzador de aplicaciones y buscador difuso nativo de Wayland, inspirado en `rofi` y `dmenu`."
content_hash: a1ec16aa8b24451e988ecb72671c999eb16da453
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/fuzzel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fuzzel

Un lanzador de aplicaciones y buscador difuso nativo de Wayland, inspirado en `rofi` y `dmenu`.
Más información: <https://codeberg.org/dnkl/fuzzel>.

- Ejecuta aplicaciones:

`fuzzel`

- Ejecuta `fuzzel` en modo dmenu:

`fuzzel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--dmenu</span>

- Muestra un menú con la salida del comando `ls`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>` | fuzzel -d`

- Muestra un menú con elementos personalizados separados por una nueva línea (`\n`):

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rojo</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verde</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">azul</span>`" | fuzzel -d`

- Permite al usuario elegir entre varios elementos y guarda el seleccionado en un archivo:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rojo</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verde</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">azul</span>`" | fuzzel -d > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color.txt</span>

- Restablece el recuento de aplicaciones utilizadas (directorio de caché por defecto: `$XDG_CACHE_HOME/fuzzel`):

`rm -v $HOME/.cache/fuzzel`

- Inicia `fuzzel` en un monitor específico, vea `wlr-randr` o `swaymsg -t get_outputs`:

`fuzzel -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DP-1</span>`"`

- Utilice `fuzzel` para realizar una búsqueda en línea:

`fuzzel -d -l 0 --placeholder "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Escriba su búsqueda</span>`" | sed 's/^/\«/g;s/$/\»/g' | xargs firefox --search`
