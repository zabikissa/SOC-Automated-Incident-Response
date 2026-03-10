
# SOC Automated Incident Response Lab

**Auteur : Wilfrid**

Laboratoire SOC complet pour **détection et réponse automatisée aux incidents malware** sur endpoints, utilisant **Splunk, SOAR Phantom et ClamAV**.  
Le projet comprend des **playbooks Python, scripts endpoints, SPL, alertes et documentation complète** pour un environnement de formation SOC ou de test de détection.

---

## 📂 Structure du dépôt

| Dossier | Contenu |
|---------|---------|
| `docs/` | Documentation, tutoriels et guides d’installation |
| `splunk/` | Requêtes SPL, alertes, mapping CEF pour SOAR Phantom |
| `soar/` | Playbooks Phantom, apps et workflows automatisés |
| `endpoint/` | Scripts pour endpoints simulant des incidents malware |
| `images/` | Screenshots, diagrammes et illustrations du lab |

---

##  Fonctionnalités principales

- **Collecte et corrélation des logs** avec Splunk Universal Forwarder  
- **Création d’alertes et mapping CEF** vers SOAR Phantom pour automatisation  
- **Playbooks Python** pour enrichissement (VirusTotal) et gestion d’artefacts  
- **Simulation d’incidents malware** via ClamAV sur endpoints  
- **Documentation complète** pour mise en place et utilisation du lab  

---

##  Technologies utilisées

- Splunk Enterprise, Splunk SOAR Phantom  
- ClamAV, Python, Ubuntu/Linux  
- Playbooks Python et scripts endpoint  
- Cron, dashboards, rapports  

---
