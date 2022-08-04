---
layout: page
title: common/sn (English)
description: "Mono StrongName utility for signing and verifying IL assemblies."
content_hash: ea3e58d1eee5cf35810d73295a199fb73f1e17ae
---
# sn

Mono StrongName utility for signing and verifying IL assemblies.
More information: <https://manned.org/sn>.

- Generate a new StrongNaming key:

`sn -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.snk</span>

- Re-sign an assembly with the specified private key:

`sn -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key_pair.snk</span>

- Show the public key of the private key that was used to sign an assembly:

`sn -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.exe</span>

- Extract the public key to a file:

`sn -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pub</span>
