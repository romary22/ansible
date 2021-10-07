# ansible

*Read this in other languages: [English](README.md), [French](README.fr.md)

Some plugins for ansible
 - dzdo su : when you must substitute user with dzdo su to launch commands
   Example : I want to execute the command : docker ps, but my user hasn't the right to do so.
   Only the user admin_docker can do. Fortunately i can use dzdo su - adm_docker to identity myself as admin_docker,
   and then launch the command.
   This plugin does the same thing for ansible.
