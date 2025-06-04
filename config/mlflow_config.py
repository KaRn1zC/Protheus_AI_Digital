import mlflow
import os

def setup_mlflow(campagne_path, experiment_name="pipeline_monitoring"):
    """
    Configure MLflow pour utiliser le dossier monitoring/ de la campagne comme backend local.
    Args:
        campagne_path (str): Chemin du dossier de la campagne (ex: "data/campagne_1")
        experiment_name (str): Nom de l'expérience MLflow
    """
    monitoring_dir = os.path.join(campagne_path, "monitoring")
    os.makedirs(monitoring_dir, exist_ok=True)
    mlflow.set_tracking_uri(f"file://{os.path.abspath(monitoring_dir)}")
    mlflow.set_experiment(experiment_name)
    print(f"MLflow tracking URI set to: {mlflow.get_tracking_uri()}")
    exp = mlflow.get_experiment_by_name(experiment_name)
    if exp is not None:
        print(f"MLflow experiment set to: {exp.name}")
    else:
        print(f"MLflow experiment '{experiment_name}' will be created on first run.")
    return mlflow
