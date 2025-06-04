from loguru import logger
import os

def setup_loguru(campagne_path, log_filename="pipeline.log"):
    """
    Configure Loguru pour écrire les logs dans le dossier logs/ de la campagne.
    Args:
        campagne_path (str): Chemin absolu ou relatif du dossier de la campagne (ex: "data/campagne_1")
        log_filename (str): Nom du fichier de log (par défaut: "pipeline.log")
    """
    logs_dir = os.path.join(campagne_path, "logs")
    os.makedirs(logs_dir, exist_ok=True)
    log_path = os.path.join(logs_dir, log_filename)

    # Retire les handlers existants pour éviter les doublons si plusieurs setup
    logger.remove()
    # Ajoute un handler fichier (rotation quotidienne, rétention 30 jours, format lisible)
    logger.add(
        log_path,
        rotation="1 day",
        retention="30 days",
        enqueue=True,
        backtrace=True,
        diagnose=True,
        level="INFO",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )
    # (optionnel) Ajoute aussi la sortie console
    logger.add(
        lambda msg: print(msg, end=""),
        level="INFO",
        format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <level>{message}</level>"
    )
    return logger
