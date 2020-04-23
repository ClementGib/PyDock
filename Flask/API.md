## API :
__Application Programmable Interface__


<img src="https://camo.githubusercontent.com/a364f9aa763e0b5dba55b0bb0348f65a24357b89/68747470733a2f2f692e7974696d672e636f6d2f76692f5551776a7974517a6f71452f6d617872657364656661756c742e6a7067">

<p> Les requètes HTTP </p>

* GET effectue une lecture
* POST crée une donnée
* PUT met à jour une donnée
* DELETE supprime une donnée

<p> Code de retour HTTP </p>

* 200 : Succès
* 400 : Erreur de syntaxe
* 404 : Introuvable
* 403 : Interdit
* 500 : Erreur interne à l'API, il est préférable de gérer cette erreur en interne pour retourner le code adéquoit.


<p> Une API est généralement un service temps réel prévu pour être exploité par d'autre logiciel </p>


<p> Flask est un micro web Framework fait et pour Python </p>






<p>  le container va s'éxecuter avec jupyter </p>
<P> la commande suivante permet d'ajouter l'utilisateur courant au groupe Docker pour l'exploiter sans les droits administrateurs </p>

```bash 
sudo groupadd docker
sudo gpasswd -a $USER docker
```
