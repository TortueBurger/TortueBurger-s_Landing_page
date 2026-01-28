# Justifications du Projet - EliasDev (SaaS Portfolio)

## 1) Approche Mobile First
* **Priorisation** : Sur mobile, l'ordre vertical place le Hero (H1 + CTA) en premier pour capter l'attention immédiatement.
* **CTA (Call to Action)** : Le bouton "Consulter mon portfolio" est large et centré pour être facilement cliquable au pouce (touch-friendly).
* **Sobriété** : La navigation est simplifiée en haut pour laisser place au contenu principal, évitant ainsi toute distraction inutile.

## 2) Responsive & Progressive Enhancement
* **Breakpoint principal** : Choisi à `900px`. 
* **Enrichissement Desktop** : 
    * La grille de compétences passe d'une seule colonne à trois colonnes via `display: grid`.
    * Le bloc "Soft-Skills" (balise `<aside>`) est mieux espacé horizontalement.
* **Pourquoi** : Cela permet d'utiliser l'espace disponible sur grand écran sans surcharger la vue mobile qui reste épurée.

## 3) Sémantique HTML5
* **Structure** : Utilisation des balises `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>` et `<footer>` pour une structure sémantique robuste.
* **Hiérarchie des titres** : Un seul `<h1>` pour le titre principal, des `<h2>` pour chaque grande section, et des `<h3>` pour les sous-titres des cartes de compétences.

## 4) Performance & Audit
* **LCP (Largest Contentful Paint)** : L'élément le plus large identifié est l'image `#Profile_pic`.
* **Actions d'optimisation** : 
    1. Utilisation du format image optimisé.
    2. Compression des icônes de compétences pour réduire le poids total de la page.