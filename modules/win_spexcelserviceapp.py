#!/usr/bin/python
# -*- coding: utf-8 -*-

# <COPYRIGHT>
# <CODEGENMETA>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# this is a windows documentation stub.  actual code lives in the .ps1
# file of the same name

DOCUMENTATION = '''
---
module: win_spexcelserviceapp
version_added: 
short_description: 
description:
     - 
options:
  ApplicationPool:
    description:
      - 
    required: True
    default: 
    aliases: []

  Name:
    description:
      - 
    required: True
    default: 
    aliases: []

  CachingOfUnusedFilesEnable:
    description:
      - 
    required: False
    default: 
    aliases: []

  CrossDomainAccessAllowed:
    description:
      - 
    required: False
    default: 
    aliases: []

  EncryptedUserConnectionRequired:
    description:
      - 
    required: False
    default: 
    aliases: []
    choices:      - Connection      - None
  Ensure:
    description:
      - 
    required: False
    default: 
    aliases: []
    choices:      - Absent      - Present
  ExternalDataConnectionLifetime:
    description:
      - 
    required: False
    default: 
    aliases: []

  FileAccessMethod:
    description:
      - 
    required: False
    default: 
    aliases: []
    choices:      - UseFileAccessAccount      - UseImpersonation
  InstallAccount_username:
    description:
      - 
    required: False
    default: 
    aliases: []

  InstallAccount_password:
    description:
      - 
    required: False
    default: 
    aliases: []

  LoadBalancingScheme:
    description:
      - 
    required: False
    default: 
    aliases: []
    choices:      - Local      - RoundRobin      - WorkbookURL
  MemoryCacheThreshold:
    description:
      - 
    required: False
    default: 
    aliases: []

  PrivateBytesMax:
    description:
      - 
    required: False
    default: 
    aliases: []

  PsDscRunAsCredential_username:
    description:
      - 
    required: False
    default: 
    aliases: []

  PsDscRunAsCredential_password:
    description:
      - 
    required: False
    default: 
    aliases: []

  SessionsPerUserMax:
    description:
      - 
    required: False
    default: 
    aliases: []

  SiteCollectionAnonymousSessionsMax:
    description:
      - 
    required: False
    default: 
    aliases: []

  TerminateProcessOnAccessViolation:
    description:
      - 
    required: False
    default: 
    aliases: []

  ThrottleAccessViolationsPerSiteCollection:
    description:
      - 
    required: False
    default: 
    aliases: []

  TrustedFileLocations:
    description:
      - 
    required: False
    default: 
    aliases: []

  UnattendedAccountApplicationId:
    description:
      - 
    required: False
    default: 
    aliases: []

  UnusedObjectAgeMax:
    description:
      - 
    required: False
    default: 
    aliases: []

  WorkbookCache:
    description:
      - 
    required: False
    default: 
    aliases: []

  WorkbookCacheSizeMax:
    description:
      - 
    required: False
    default: 
    aliases: []

  AutoInstallModule:
    description:
      - If true, the required dsc resource/module will be auto-installed using the Powershell package manager
    required: False
    default: false
    aliases: []
    choices:      - true      - false
  AutoConfigureLcm:
    description:
      - If true, LCM will be auto-configured for directly invoking DSC resources (which is a one-time requirement for Ansible DSC modules)
    required: False
    default: false
    aliases: []
    choices:      - true      - false
