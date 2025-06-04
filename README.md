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

## Télécharger les modèles CoreML SAM2-small pour MacOS

**Installer `huggingface-cli` :**

`brew install huggingface-cli`

**Utilise la commande suivante pour télécharger tous les fichiers nécessaires directement dans ton dossier `models/sam2-small-coreml` :**

`huggingface-cli download --local-dir models/sam2-small-coreml coreml-projects/coreml-sam2-small`

**Organise ton dossier ainsi :**

```bash
models/
├── sam2-small-coreml/
│   ├── SAM2_1SmallImageEncoderFLOAT16.mlpackage
│   ├── SAM2_1SmallPromptEncoderFLOAT16.mlpackage
│   └── SAM2_1SmallMaskDecoderFLOAT16.mlpackage
```

## Télécharger et installer LightGlue + SuperPoint

**Executer ceci :**

```bash
git clone https://github.com/cvg/LightGlue.git
cd LightGlue
python -m pip install -e .
cd ..
```

**Télécharger le modèle adapté à ONNX pour une utilisation optimisée Apple Silicon :**

`https://github.com/fabio-sim/LightGlue-ONNX/releases/download/v2.0/superpoint_lightglue_pipeline.onnx`

**Place le fichier ainsi dans ton projet :**

```bash
models/
└── lightglue_superpoint/
    └── superpoint_lightglue_pipeline.onnx
```

## Utilisation de loguru dans un script de campagne

```python
from config.loguru_config import setup_loguru

logger = setup_loguru("data/campagne_1")
logger.info("Démarrage du pipeline pour campagne 1.")
```

## Utilisation de mlflow dans un script de campagne

```python
from config.mlflow_config import setup_mlflow
import mlflow

setup_mlflow("data/campagne_1")
with mlflow.start_run(run_name="run_001"):
    mlflow.log_param("param1", 42)
    mlflow.log_metric("accuracy", 0.98)
    # etc.
```





