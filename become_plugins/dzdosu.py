# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    become: dzdosu
    short_description: su with Centrify's Direct Authorize
    description:
        - This become plugins allows your remote/login user to execute commands as another user with su via the dzdo utility.
    author: Romary
    options:
        become_user:
            description: User you 'become' to execute the task
            ini:
              - section: privilege_escalation
                key: become_user
              - section: dzdosu_become_plugin
                key: user
            vars:
              - name: ansible_become_user
              - name: ansible_dzdosu_user
            env:
              - name: ANSIBLE_BECOME_USER
              - name: ANSIBLE_DZDOSU_USER
        become_exe:
            description: dzdo su -
            default: dzdo su -
            ini:
              - section: privilege_escalation
                key: become_exe
              - section: dzdosu_become_plugin
                key: executable
            vars:
              - name: ansible_become_exe
              - name: ansible_dzdosu_exe
            env:
              - name: ANSIBLE_BECOME_EXE
              - name: ANSIBLE_DZDOSU_EXE
        become_flags:
            description: Options to pass to dzdo
            default:
            ini:
              - section: privilege_escalation
                key: become_flags
              - section: dzdosu_become_plugin
                key: flags
            vars:
              - name: ansible_become_flags
              - name: ansible_dzdosu_flags
            env:
              - name: ANSIBLE_BECOME_FLAGS
              - name: ANSIBLE_DZDOSU_FLAGS
        become_pass:
            description: Options to pass to dzdo
            required: False
            vars:
              - name: ansible_become_password
              - name: ansible_become_pass
              - name: ansible_dzdosu_pass
            env:
              - name: ANSIBLE_BECOME_PASS
              - name: ANSIBLE_DZDOSU_PASS
            ini:
              - section: dzdosu_become_plugin
                key: password
"""

from ansible.plugins.become import BecomeBase


class BecomeModule(BecomeBase):

    name = 'dzdosu'

    # messages for detecting prompted password issues
    fail = ('Sorry, try again.',)

    def build_become_command(self, cmd, shell):
        super(BecomeModule, self).build_become_command(cmd, shell)

        if not cmd:
            return cmd

        becomecmd = self.get_option('become_exe') or self.name

        flags = self.get_option('become_flags') or ''
        if self.get_option('become_pass'):
            self.prompt = '[dzdo su via ansible, key=%s] password:' % self._id
            #flags = '%s -p "%s"' % (flags.replace('-n', ''), self.prompt)

        become_user = self.get_option('become_user')
        user = '%s' % (become_user) if become_user else ''

        return ' '.join(['(', becomecmd, user, flags,"<<eof\n", self._build_success_command(cmd, shell), "\neof\n)"])
