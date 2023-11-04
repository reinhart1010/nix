---
layout: page
title: common/clang-tidy (Deutsch)
description: "Ein LLVM-basierter C/C++ Linter zum Finden von Stilverletzungen, Bugs und Sicherheitsmängeln durch statische Codeanalyse."
content_hash: bf9b85130f0430fc12f873789d6a12da4fc98124
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/common/clang-tidy.html
    icon: bi bi-globe
---
# clang-tidy

Ein LLVM-basierter C/C++ Linter zum Finden von Stilverletzungen, Bugs und Sicherheitsmängeln durch statische Codeanalyse.
Weitere Information: <https://clang.llvm.org/extra/clang-tidy/>.

- Führe die Standard-Checks für eine Quelldatei aus:

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>

- Prüfe nur ob eine Datei den `cppcoreguidelines` Checks entspricht:

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>` -checks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-*,cppcoreguidelines-*</span>

- Liste alle verfügbaren Checks auf:

`clang-tidy -checks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>` -list-checks`

- Lege defines und includes als Kompilierungsoptionen fest (nach `--`):

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.cpp</span>` -- -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mein_projekt/include</span>` -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">definitions</span>
