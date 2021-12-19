---
layout: page
title: common/sn (English)
description: "Mono StrongName utility for signing and verifying IL assemblies."
content_hash: c880c3e93188c3b24a5b38309ae29d5cc964a3fe
---
# sn

Mono StrongName utility for signing and verifying IL assemblies.

- Generate a new StrongNaming key:

`sn -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.snk</span>

- Re-sign an assembly with the specified private key:

`sn -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key_pair.snk</span>

- Show the public key of the private key that was used to sign an assembly:

`sn -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.exe</span>

- Extract the public key to a file:

`sn -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pub</span>
