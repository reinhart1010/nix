---
layout: page
title: common/monop (English)
description: "Finds and displays signatures of Types and methods inside .NET assemblies."
content_hash: 17a2c3bd1a508c8ab80d757e421f028712c4c400
---
# monop

Finds and displays signatures of Types and methods inside .NET assemblies.
More information: <https://manned.org/monop>.

- Show the structure of a Type built-in of the .NET Framework:

`monop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">System.String</span>

- List the types in an assembly:

`monop -r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.exe</span>

- Show the structure of a Type in a specific assembly:

`monop -r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Namespace.Path.To.Type</span>

- Only show members defined in the specified Type:

`monop -r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>` --only-declared `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Namespace.Path.To.Type</span>

- Show private members:

`monop -r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>` --private `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Namespace.Path.To.Type</span>

- Hide obsolete members:

`monop -r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>` --filter-obsolete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Namespace.Path.To.Type</span>

- List the other assemblies that a specified assembly references:

`monop -r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>` --refs`
