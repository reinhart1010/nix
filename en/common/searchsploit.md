---
layout: page
title: common/searchsploit (English)
description: "Searchsploit searches exploit database's database for exploits, shellcodes and/or papers."
content_hash: 6e4fdde03530fb10c6c0c1ea49f2b2899732bb33
---
# searchsploit

Searchsploit searches exploit database's database for exploits, shellcodes and/or papers.
If known version numbers are used as search terms, exploits for both the exact version and others whose version range covers the one specified are shown.
More information: <https://www.exploit-db.com/searchsploit>.

- Search for an exploit, shellcode, or paper:

`searchsploit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_terms</span>

- Search for a known specific version, e.g. sudo version 1.8.27:

`searchsploit sudo 1.8.27`

- Show the exploit-db link to the found resources:

`searchsploit --www `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_terms</span>

- Make a copy of the resource to the current directory (requires the number of the exploit):

`searchsploit --mirror `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exploit_number</span>

- Open the resource to read with the pager defined in the `$PAGER` environment variable:

`searchsploit --explore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exploit_number</span>

- Update the local exploit database:

`searchsploit --update`
