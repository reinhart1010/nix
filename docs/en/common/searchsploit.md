---
layout: page
title: common/searchsploit (English)
description: "Search Exploit Database for exploits, shellcodes and/or papers."
content_hash: fade5599ea176658541d5b6fee8aa952cd8634db
last_modified_at: 2024-02-21
tldri18n_status: 2
---
# searchsploit

Search Exploit Database for exploits, shellcodes and/or papers.
If known version numbers are used as search terms, exploits for both the exact version and others whose version range covers the one specified are shown.
More information: <https://www.exploit-db.com/searchsploit>.

- Search for an exploit, shellcode, or paper:

`searchsploit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_terms</span>

- Search for a known specific version, e.g. sudo version 1.8.27:

`searchsploit sudo 1.8.27`

- Show the exploit-db link to the found resources:

`searchsploit --www `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_terms</span>

- Copy ([m]irror) the resource to the current directory (requires the number of the exploit):

`searchsploit --mirror `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exploit_number</span>

- E[x]amine the resource, using the pager defined in the `$PAGER` environment variable:

`searchsploit --examine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exploit_number</span>

- [u]pdate the local Exploit Database:

`searchsploit --update`

- Search for the [c]ommon [v]ulnerabilities and [e]xposures (CVE) value:

`searchsploit --cve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2021-44228</span>

- Check results in `nmap`'s XML output with service version (`nmap -sV -oX nmap-output.xml`) for known exploits:

`searchsploit --nmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/nmap-output.xml</span>
