# dzdosu

## Synopsis

    This become plugins allows your remote/login user to execute commands as another user via the dzdo su.

## Parameters
|Parameter|Choices/Defaults|Configuration|Comments|
|---------|----------------|-------------|--------|
|**become_exe**<br/>string|**Default:**<br/>"dzdosu"|ini entries:<br/>[privilege_escalation]<br/>become_exe = dzdosu<br/><br/>[dzdosu_become_plugin]<br/>executable = dzdosu<br/>env:ANSIBLE_BECOME_EXE<br/>env:ANSIBLE_DZDOSU_EXE<br/>var: ansible_become_exe<br/>var: ansible_dzdosu_exe|Dzdosu executable|
|**become_flags**<br/>string||ini entries:<br/><br/>[privilege_escalation]<br/>become_flags =<br/><br/>[dzdosu_become_plugin]<br/>flags =<br/>env:ANSIBLE_BECOME_FLAGS<br/>env:ANSIBLE_DZDOSU_FLAGS<br/>var: ansible_become_flags<br/>var: ansible_dzdsuo_flags|Options to pass to dzdosu|
|**become_pass**<br/>string||ini entries:<br/><br/>[dzdosu_become_plugin]<br/>password = None<br/>env:ANSIBLE_BECOME_PASS<br/>env:ANSIBLE_DZDOSU_PASS<br/>var: ansible_become_password<br/>var: ansible_become_pass<br/>var: ansible_dzdosu_pass|Password to dzdosu|
|**become_user**<br/>string||ini entries:<br/><br/>[privilege_escalation]<br/>become_user = None<br/><br/>[dzdosu_become_plugin]<br/>user = None<br/>env:ANSIBLE_BECOME_USER<br/>env:ANSIBLE_DZDOSU_USER<br/>var: ansible_become_user<br/>var: ansible_dzdosu_user|User you 'become' to execute the task|
