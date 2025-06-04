# Projet Protheus AI Digital

```bash
.
├── config/
│   ├── loguru_config.py         # Configuration globale du logger Loguru (format, niveaux, handlers, etc.)
│   └── mlflow_config.py         # Configuration globale de MLflow (tracking, endpoints, paramètres d’expérimentation)
├── data/
│   └── campagne_1/
│       ├── guideline/           # Guideline PDF du client pour la campagne (fichier source)
│       ├── hires_originals/     # Images haute résolution originales à associer et recadrer
│       ├── images/              # Images extraites (basse résolution) à partir des pages du PDF
│       ├── logs/                # Logs spécifiques à la campagne (exécution, erreurs, suivi)
│       ├── meta/                # Métadonnées intermédiaires (JSON: mapping images-ratios, résultats OCR, associations, etc.)
│       ├── monitoring/          # Rapports de monitoring, métriques de pipeline, sorties MLflow pour la campagne
│       ├── output/
│       │   ├── crop_hires/      # Images haute résolution recadrées selon les ratios demandés
│       │   └── crop_lowres/     # Images basse résolution recadrées (prévisualisation, validation)
│       ├── pages/               # Images des pages extraites du PDF (format PNG/JPEG)
│       ├── segmentation/        # Masques, bounding boxes, visualisations issues de la segmentation (SAM2, etc.) (PNG et JSON selon les données)
│       ├── tmp/                 # Fichiers temporaires ou intermédiaires (debug, étapes de traitement)
│       └── validation/          # Rapports et visualisations de contrôle qualité, checklist de conformité visuelle
├── models/                      # Modèles IA utilisés (SAM2-small CoreML, LightGlue + Superpoint, etc.), fichiers CoreML, checkpoints, etc.
├── README.md                    # Documentation principale du projet, instructions d’installation et d’utilisation
├── requirements.txt             # Dépendances Python du projet
├── scripts/                     # Scripts Python utilitaires, launchers de pipeline, notebooks de debug, etc.
```





