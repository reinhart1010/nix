---
layout: page
title: windows/enable-pnpdevice (English)
description: "The Enable-PnpDevice cmdlet enables a Plug and Play (PnP) device. You must use an Administrator account to enable a device."
content_hash: 676725d863de97735f086c73278a5dc42613922e
last_modified_at: 2024-06-09
tldri18n_status: 2
---
# Enable-PnpDevice

The Enable-PnpDevice cmdlet enables a Plug and Play (PnP) device. You must use an Administrator account to enable a device.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/pnpdevice/enable-pnpdevice>.

- Enable a device:

`Enable-PnpDevice -InstanceId 'RETRIEVED USING Get-PnpDevice COMMAND'`

- Enable all disabled PnP devices:

`Get-PnpDevice | Where-Object {$_.Problem -eq 22} | Enable-PnpDevice`

- Enable a device without confirmation:

`Enable-PnpDevice -InstanceId 'RETRIEVED USING Get-PnpDevice COMMAND' -Confirm:$False`

- Dry run of what would happen if the cmdlet runs:

`Enable-PnpDevice -InstanceId 'USB\VID_5986&;PID_0266&;MI_00\7&;1E5D3568&;0&;0000' -WhatIf:$True`
