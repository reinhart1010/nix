---
layout: page
title: common/pake (English)
description: "Turn any webpage into a desktop app with Rust/Tauri."
content_hash: 5f937d00ab2f682e5f2ec238fbfb3a467c0f4d07
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pake

Turn any webpage into a desktop app with Rust/Tauri.
More information: <https://github.com/tw93/Pake>.

- Package a web page:

`pake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/</span>

- Package a web page with a specific window size:

`pake --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800</span>` --height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">600</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/</span>

- Package a web page with a custom application name and icon:

`pake --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Google</span>` --icon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/icon.ico</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/</span>

- Package a web page with a non-resizable window:

`pake --no-resizable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/</span>

- Package a web page with fullscreen mode:

`pake --fullscreen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/</span>

- Package a web page with a transparent title bar:

`pake --transparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.google.com/</span>
