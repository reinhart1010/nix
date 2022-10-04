---
layout: page
title: common/csc (italiano)
description: "Compilatore per Microsoft C#."
content_hash: 1725c678707877f01eea59d1ce4e3cb408674f9b
related_topics:
  - title: English version
    url: /en/common/csc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csc.html
    icon: bi bi-globe
---
# csc

Compilatore per Microsoft C#.
Maggiori informazioni: <https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/command-line-building-with-csc-exe>.

- Compila uno o più file C# in un eseguibile da command-line:

`csc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_input_a.cs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_input_b.cs</span>

- Specifica il nome del file output:

`csc /out:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/nome_file_output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_input.cs</span>

- Compila in una libreria `.dll` invece che in un eseguibile:

`csc /target:library `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_input.cs</span>

- Referenzia un altro assembly:

`csc /reference:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/libreria.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_input.cs</span>

- Includi una risorsa:

`csc /resource:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_risorsa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_input.cs</span>

- Genera una documentazione XML automaticamente:

`csc /doc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/documentazione.xml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_input.cs</span>

- Specifica un'icona:

`csc /win32icon:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/icona.ico</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_input.cs</span>

- Firma un assembly con un nome sicuro utilizzando una chiave:

`csc /keyfile:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/chiave.snk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_input.cs</span>
