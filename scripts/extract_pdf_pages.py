import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import fitz  # PyMuPDF
from PIL import Image
from config.loguru_config import setup_loguru

def extract_pdf_pages(campagne_path, pdf_filename=None, dpi=72, jpeg_quality=100):
    """
    Extrait chaque page du PDF de guideline en image JPEG haute qualité à 72 DPI dans le dossier pages/ de la campagne.
    Args:
        campagne_path (str): Chemin du dossier campagne (ex: "data/240910_CRUISE25")
        pdf_filename (str): Nom du fichier PDF (par défaut, prend le premier PDF trouvé dans guideline/)
        dpi (int): Résolution de rendu (défaut: 72)
        jpeg_quality (int): Qualité JPEG (100 = max, sans perte perceptible)
    """
    logger = setup_loguru(campagne_path, log_filename="extract_pdf_pages.log")

    guideline_dir = os.path.join(campagne_path, "guideline")
    pages_dir = os.path.join(campagne_path, "pages")
    os.makedirs(pages_dir, exist_ok=True)

    # Trouve le PDF à traiter si non spécifié
    if pdf_filename is None:
        pdfs = [f for f in os.listdir(guideline_dir) if f.lower().endswith(".pdf")]
        if not pdfs:
            logger.error(f"Aucun PDF trouvé dans {guideline_dir}")
            return
        pdf_filename = pdfs[0]
    pdf_path = os.path.join(guideline_dir, pdf_filename)

    logger.info(f"Ouverture du PDF : {pdf_path}")
    doc = fitz.open(pdf_path)
    logger.info(f"{doc.page_count} pages détectées.")

    for i, page in enumerate(doc):
        # Utilise directement le paramètre dpi pour obtenir une image à 72 DPI
        pix = page.get_pixmap(dpi=dpi, alpha=False)
        mode = "RGB" if pix.n < 4 else "RGBA"
        img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
        if img.mode == "RGBA":
            img = img.convert("RGB")  # JPEG ne supporte pas l'alpha

        out_name = f"page_{i+1:03d}.jpeg"
        out_path = os.path.join(pages_dir, out_name)
        # Sauvegarde JPEG qualité maximale, sans sous-échantillonnage chroma, avec profil ICC si présent
        img.save(
            out_path,
            "JPEG",
            quality=jpeg_quality,
            subsampling=0,  # 4:4:4, pas de sous-échantillonnage
            icc_profile=img.info.get("icc_profile", None),
            dpi=(dpi, dpi),
            optimize=True,
        )
        logger.info(f"Page {i+1} extraite : {out_path}")

    logger.success(f"Extraction terminée : {doc.page_count} pages enregistrées dans {pages_dir}")
    doc.close()

if __name__ == "__main__":
    # Utilisation : python extract_pdf_pages.py data/240910_CRUISE25 [nom_pdf_optionnel]
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf_pages.py <chemin_dossier_campagne> [nom_pdf]")
        sys.exit(1)
    campagne_path = sys.argv[1]
    pdf_filename = sys.argv[2] if len(sys.argv) > 2 else None
    extract_pdf_pages(campagne_path, pdf_filename)
