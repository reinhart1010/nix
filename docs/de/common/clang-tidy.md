---
layout: page
title: common/clang-tidy (Deutsch)
description: "Ein LLVM-basierter C/C++ Linter zum Finden von Stilverletzungen, Bugs und Sicherheitsmängeln durch statische Codeanalyse."
content_hash: 222a3c31c1f9b8c28efae3c23f8a7bca65d58bf8
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/common/clang-tidy.html
    icon: bi bi-globe
---
# clang-tidy

Ein LLVM-basierter C/C++ Linter zum Finden von Stilverletzungen, Bugs und Sicherheitsmängeln durch statische Codeanalyse.
Weitere Informationen: <https://clang.llvm.org/extra/clang-tidy/>.

- Führe die Standard-Checks für eine Quelldatei aus:

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>

- Prüfe nur ob eine Datei den `cppcoreguidelines` Checks entspricht:

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>` -checks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-*,cppcoreguidelines-*</span>

- Liste alle verfügbaren Checks auf:

`clang-tidy -checks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>` -list-checks`

- Lege defines und includes als Kompilierungsoptionen fest (nach `--`):

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>` -- -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mein_projekt/include</span>` -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">definitions</span>
