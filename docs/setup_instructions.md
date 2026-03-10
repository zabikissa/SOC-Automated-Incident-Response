# Installation et configuration

## Endpoint Linux (victime)
1. Installer ClamAV : `sudo apt install clamav clamav-daemon -y`
2. Mettre à jour la base de virus : `sudo freshclam`
3. Vérifier le daemon : `sudo systemctl status clamav-daemon`
4. Installer Splunk Forwarder et configurer pour envoyer logs à Splunk Master

## Splunk Master
1. Télécharger Splunk Enterprise
2. Décompresser et démarrer : `/opt/splunk/bin/splunk start --accept-license`
3. Créer index `clamav_logs` pour récupérer logs ClamAV
4. Créer alertes et mapping CEF pour Phantom
