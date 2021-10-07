# ansible

*Lire ceci dans d'autre langues: [Anglais](README.md), [Français](README.fr.md)

Quelques plugins pour ansible
 - dzdo su : quand vous devez vous identier avec `dzdo su` pour lancer certaines commandes  
   Exemple : Je veux éxécuter la commande docker ps, mais mon utilisateur local n'a pas ce droit.  
   Seul l'utilisateur admin_docker peut le faire.  
   Heureusement je peux m'identifier en tant que admin_docker avec `dzdo su - admin_docker`, puis lancer la commande.  
   Ce plugin permet de faire ceci avec ansible.  
