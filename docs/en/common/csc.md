---
layout: page
title: common/csc (English)
description: "The Microsoft C# Compiler."
content_hash: 758a2f767c2864e0635e5f44c26839bdfc86ed23
related_topics:
  - title: italiano version
    url: /it/common/csc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csc.html
    icon: bi bi-globe
---
# csc

The Microsoft C# Compiler.
More information: <https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/command-line-building-with-csc-exe>.

- Compile one or more C# files to a CIL executable:

`csc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file_a.cs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file_b.cs</span>

- Specify the output filename:

`csc /out:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.cs</span>

- Compile into a `.dll` library instead of an executable:

`csc /target:library `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.cs</span>

- Reference another assembly:

`csc /reference:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/library.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.cs</span>

- Embed a resource:

`csc /resource:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/resource_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.cs</span>

- Automatically generate XML documentation:

`csc /doc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.cs</span>

- Specify an icon:

`csc /win32icon:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/icon.ico</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.cs</span>

- Strongly-name the resulting assembly with a keyfile:

`csc /keyfile:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/keyfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.cs</span>
