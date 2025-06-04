```markdown
# Méthodologie de Recadrage Intelligent pour Préservation de Direction Artistique

Voici une logique de réflexion systématique et universelle pour analyser n'importe quelle image de guideline et créer des versions recadrées qui préservent parfaitement la direction artistique.

## Analyse Préliminaire de l'Image Guideline

### Étape 1 : Identification de la Structure Compositionnelle

**Grille d'Analyse Visuelle** :
Pour chaque image guideline, appliquer cette grille d'analyse :

1. SUJET PRINCIPAL : Qu'est-ce qui attire immédiatement l'œil ?
2. POSITION DU SUJET : Où se situe-t-il dans l'image (règle des tiers, centré, décentré) ?
3. RAPPORT TAILLE/CADRE : Quelle proportion du cadre occupe le sujet principal ?
4. ÉLÉMENTS SECONDAIRES : Quels autres éléments contribuent à la composition ?
5. ESPACES NÉGATIFS : Où se trouvent les zones de respiration importantes ?

### Étape 2 : Cartographie des Zones Critiques

**Système de Priorité à 3 Niveaux** :

**Zone A - Intouchable** (Rouge) :
- Sujet principal complet
- Éléments de gestuelle ou d'expression importants
- Objets portés/tenus par le sujet

**Zone B - Modulable** (Orange) :
- Éléments contextuels significatifs
- Parties d'architecture ou décor qui participent à l'ambiance
- Espaces de respiration directement liés au sujet

**Zone C - Sacrifiable** (Vert) :
- Arrière-plan générique
- Zones répétitives ou sans information cruciale
- Espaces excédentaires

## Méthodologie de Calcul du Recadrage

### Technique des Ratios Proportionnels Conservés

**Formule de Base** :
Pour passer d'un format original (L₁ × H₁) vers un nouveau format (L₂ × H₂), calculer :

Ratio original = L₁/H₁
Ratio cible = L₂/H₂

Si Ratio_cible > Ratio_original : Format plus large (contrainte hauteur)
Si Ratio_cible < Ratio_original : Format plus haut (contrainte largeur)

### Algorithme de Positionnement Intelligent

**Étape 1 : Analyse des Distances Relatives**

Pour le sujet principal, mesurer :
- Distance au bord gauche / Largeur totale = Ratio_G
- Distance au bord droit / Largeur totale = Ratio_D  
- Distance au bord haut / Hauteur totale = Ratio_H
- Distance au bord bas / Hauteur totale = Ratio_B

**Étape 2 : Application de la Règle de Conservation**

Selon la contrainte de format (largeur ou hauteur), appliquer la **règle de conservation prioritaire** :

**Si contrainte LARGEUR** (format plus haut) :
1. Conserver Ratio_G et Ratio_D en priorité
2. Ajuster la hauteur pour maintenir le sujet complet
3. Équilibrer Ratio_H et Ratio_B selon l'espace disponible

**Si contrainte HAUTEUR** (format plus large) :
1. Conserver Ratio_H et Ratio_B en priorité  
2. Ajuster la largeur pour maintenir le sujet complet
3. Équilibrer Ratio_G et Ratio_D selon l'espace disponible

## Système de Validation de la Direction Artistique

### Checklist de Cohérence Visuelle

**1. Test de Lecture Visuelle** :
- Le regard suit-il le même parcours que dans l'original ?
- La hiérarchie visuelle est-elle préservée ?
- L'impact émotionnel reste-t-il identique ?

**2. Test de Proportions** :
- Le sujet conserve-t-il sa présence relative dans le cadre ?
- Les espaces de respiration respectent-ils l'intention originale ?
- L'équilibre compositonnel est-il maintenu ?

**3. Test de Contextualisation** :
- Les éléments de contexte essentiels sont-ils préservés ?
- L'ambiance générale de l'image est-elle conservée ?
- Le style de cadrage correspond-il à la direction artistique ?

## Workflow Pratique Universel

### Phase 1 : Diagnostic

1. Identifier le type de direction artistique
2. Localiser le sujet principal et mesurer ses distances aux bords
3. Cartographier les zones A, B, C
4. Calculer le ratio de contrainte (largeur vs hauteur)

### Phase 2 : Calcul

1. Appliquer la règle de conservation appropriée
2. Calculer les nouvelles coordonnées de cadrage
3. Vérifier que les zones A restent intactes
4. Optimiser l'inclusion des zones B selon l'espace disponible

### Phase 3 : Validation

1. Appliquer la checklist de cohérence visuelle
2. Comparer visuellement avec l'original
3. Ajuster si nécessaire (micro-corrections)
4. Valider la préservation de la direction artistique

Cette méthodologie garantit que peu importe l'image guideline et le ratio demandé, la direction artistique sera systématiquement préservée grâce à une analyse structurée et des règles de calcul adaptatives.
```

-------------------------------------------------------------

Voici le plan détaillé des étapes que l'on est censé réaliser pour réussir à mettre en place une pipeline qui répond à notre projet :
```markdown
# Étapes détaillées

## 1. **Extraction des pages**
- Extraire chaque page du PDF en image (PNG/JPEG) avec PyMuPDF.

## 2. **Segmentation générale des pages avec SAM2-small CoreML**
- **Utilisation de SAM2-small CoreML** :
  - Appliquer le modèle sur chaque page pour segmenter automatiquement toutes les zones d’image présentes (photos, illustrations, etc.).
  - Cette segmentation permet d’isoler chaque image, même si elles sont proches ou partiellement superposées.

## 3. **Découpage des images individuelles**
- Utiliser les masques/bounding boxes générés par SAM2 pour extraire chaque image individuelle de la page et les stocker.
- Cette étape garantit que chaque image extraite correspond bien à une seule illustration/photo, sans confusion avec les autres éléments visuels de la page.

## 4. **Extraction des demandes de cadrage (ratios)**
- Extraire le texte de la page pour repérer les demandes de ratio/cadrages (Apple Vision Framework Python Utilities + Regex Python).
- Associer les ratios/cadrages à chaque image extraite :
  - Par proximité spatiale (ratios proches d’une image)
  - Ou globalement (ratios à appliquer à toutes les images de la page)

## 5. **Segmentation artistique par image**

**Objectif** : Localiser précisément le sujet principal et cartographier les zones critiques (A, B, C) pour chaque image extraite.

### **Outils et méthodes à utiliser**
- **SAM2-small CoreML** :
  - Appliquer le modèle sur chaque image pour obtenir des masques de segmentation fine.
  - Identifier le(s) sujet(s) principal(aux) : le masque le plus grand ou le plus saillant correspond généralement au sujet principal.
  - Extraire les coordonnées du sujet (bounding box, centre de masse, contours).
- **OpenCV** :
  - Calculer les distances du sujet principal aux bords de l’image (pour la règle de conservation des proportions).
  - Générer des visualisations pour valider la cartographie des zones critiques (A, B, C).
- **Logique Python personnalisée** :
  - Appliquer la grille d’analyse visuelle : déterminer la position du sujet (règle des tiers, centré/décentré), rapport taille/cadre, espaces négatifs, etc.
  - Classifier les zones en A (intouchable), B (modulable), C (sacrifiable) selon la segmentation et la composition.

## **Étape 6 : Génération des crops basse résolution**

**Objectif** : Calculer et appliquer le crop optimal pour chaque ratio demandé, en préservant la direction artistique de l’original.

### **Outils et méthodes à utiliser**
- **OpenCV** :
  - Calculer les nouveaux cadres de crop selon les ratios demandés et la méthodologie de conservation des proportions (contrainte largeur ou hauteur).
  - Appliquer le crop sur l’image basse résolution.
  - Redimensionner le crop au format cible.
- **Logique Python personnalisée** :
  - Utiliser les distances relatives (calculées à l’étape 5) pour appliquer la règle de conservation prioritaire :  
    - Si contrainte largeur, préserver les ratios haut/bas ;  
    - Si contrainte hauteur, préserver les ratios gauche/droite.
  - Vérifier que la zone A (sujet principal) est intégralement préservée dans le crop.
  - Optimiser l’inclusion des zones B et minimiser la coupe des zones C.
  - Appliquer la checklist de validation (lecture visuelle, proportions, contexte). 

### Recommandations**
- **SAM2-small CoreML** est indispensable pour la localisation précise du sujet et la cartographie des zones critiques.
- **OpenCV** est incontournable pour tous les calculs de distances, l’application des crops et la validation visuelle.
- **La logique de conservation des proportions et la cartographie des zones** doivent être implémentées en Python, en s’appuyant sur les sorties de SAM2 et OpenCV.

## 7. **Matching avec l’image haute résolution**
**LightGlue + SuperPoint** : 
  - Identifier l’image haute résolution d’origine correspondante à l'image basse résolution généré que l'on veut comparer.

### **Gestion de la rotation et du positionnement**
  - Détecter si l'image basse résolution a une rotation différente de l'image haute résolution
  - Si c'est le cas, appliquer la rotation nécessaire à l’image haute résolution pour correspondre à l’orientation de la version basse résolution.

### **Application du crop sur l’image haute résolution**
  - matching avancé de points d’intérêt et garantir que le crop soit appliqué exactement au bon endroit lors du passage à la haute résolution (rotation, perspective, etc.). 

## 8. **Contrôle qualité et livraison**
- Vérification, logs, livraison.
```
----------------------------------------------------------------------------

Voici les différents modèles d'IA et librairies python que je souhaite utiliser pour ce projet :
```markdown
PyMuPDF, Apple Vision Framework Python Utilities (OCR) + Regex (Complet pour détecter toutes les variantes d'écritures d'indications de résolutions présentes), OpenCV, SAM2-small CoreML, LightGlue + SuperPoint, Loguru, MLflow.
```

----------------------------------------------------------------------------

Voici le contexte de mon programme que je veux développer :
```markdown
## Développement d’un Programme Python d’Extraction et de Traitement Automatique de Guidelines PDF pour Campagnes Publicitaires

### Contexte
Je souhaite développer un programme Python utilisant un ou plusieurs modèles d’IA open source, capable de traiter automatiquement des fichiers PDF de guidelines reçus de clients pour des campagnes publicitaires. Ces fichiers PDF comportent plusieurs pages, chaque page contenant :

- Une ou plusieurs images de photoshoot (basse résolution)
- Une ou plusieurs demandes de ratios/cadrages exprimées sous différentes formes (ex : “1560x780”, “1920*1080”, etc.), placées n'importe où sur la page

### Objectifs
Le programme doit :

1. **Détecter et extraire toutes les images présentes sur chaque page du PDF**
2. **Détecter et extraire toutes les demandes de ratios/cadrages sur chaque page, peu importe leur emplacement ou la forme de l’expression**
3. **Associer correctement chaque demande de ratio uniquement aux images de la même page**
4. **Redimensionner automatiquement chaque image basse résolution selon tous les ratios demandés sur la page**
5. **Pour chaque nouvelle image redimensionnée, la faire correspondre (“matching”) à l’image haute résolution d’origine (stockée sur un cloud)**
6. **Générer une copie de l’image haute résolution d’origine, recadrée et/ou pivotée pour correspondre exactement au cadrage/ratio demandé**
7. **Être capable de détecter et corriger une éventuelle rotation entre l’image basse résolution et l’image haute résolution pour garantir un matching parfait**
8. **Répéter ce processus pour chaque image et chaque ratio de chaque page, de façon fiable, adaptative et répétitive, quel que soit le format ou la structure du PDF fourni**

### Contraintes et Spécificités
- Les demandes de ratio doivent être strictement associées aux images de leur page respective, sans croisement entre pages
- Les formats de ratio peuvent varier dans leur écriture (par exemple : “1560x780”, “1560 x 780”, “1560*780”, etc.)
- Les images de la guideline peuvent être orientées différemment de l’image haute résolution d’origine : le programme doit gérer la détection et la correction de la rotation pour un matching optimal
- La solution doit s’appuyer sur des modèles d’IA open source pour garantir fiabilité, adaptabilité et évolutivité.

## Contexte Technique
**Plateforme cible** :  
Mac modernes équipés de puces Apple Silicon (M1/M2/M3/M4) avec 16+ Go de RAM  
**Système d'exploitation** : macOS Sequoia 15.5+  
**Version Python** : 3.12+ (ARM-native)
```