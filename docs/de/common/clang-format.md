---
layout: page
title: common/clang-format (Deutsch)
description: "Programm zum Auto-Formatieren von C/C++/Java/JavaScript/Objective-C/Protobuf/C#-Code."
content_hash: bad922b1f873901bb5af8b83717ec68ce2212d65
last_modified_at: 2024-04-19
related_topics:
  - title: English version
    url: /en/common/clang-format.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clang-format

Programm zum Auto-Formatieren von C/C++/Java/JavaScript/Objective-C/Protobuf/C#-Code.
Weitere Informationen: <https://clang.llvm.org/docs/ClangFormat.html>.

- Formatiere eine Datei und schreibe das Ergebnis nach `stdout`:

`clang-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>

- Überschreibe eine Datei mit ihrem formatierten Inhalt:

`clang-format -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>

- Formatiere eine Datei mit einem bestimmten Code-Stil:

`clang-format --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>

- Formatiere eine Datei mit der `.clang-format`-Datei aus einem der Überverzeichnisse der Quelldatei:

`clang-format --style=file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>

- Generiere eine eigene `.clang-format`-Datei:

`clang-format --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit</span>` --dump-config > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.clang-format</span>
