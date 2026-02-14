import os
import sys
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

from src.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from src.entity.config_entity import ModelTrainerConfig

from src.utils import get_classification_matric
from src.utils import TrainingModel, load_pickle_obj, save_pickle_obj, load_numpy_obj

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier
)

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score


class ModelTrainer:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact,
                 model_trainer_config: ModelTrainerConfig):
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_config = model_trainer_config

    # ---------------------------------------------------
    # Model Evaluation Function
    # ---------------------------------------------------
    def evaluate_model(self, models, params, x_train, x_test, y_train, y_test):

        report = {}
        trained_models = {}

        try:
            for model_name, model in models.items():

                logging.info(f"Training {model_name}")

                param = params[model_name]

                gs = GridSearchCV(model, param, cv=3)
                gs.fit(x_train, y_train)

                best_model = gs.best_estimator_

                y_test_pred = best_model.predict(x_test)

                test_score = accuracy_score(y_test, y_test_pred)

                report[model_name] = test_score
                trained_models[model_name] = best_model

            return report, trained_models

        except Exception as e:
            raise CustomException(e, sys)

    # ---------------------------------------------------
    # Main Training Pipeline
    # ---------------------------------------------------
    def initiate_model_training(self):

        try:
            train_data_path = self.data_transformation_artifact.train_data_arr_path
            test_data_path = self.data_transformation_artifact.test_data_arr_path

            train_data = load_numpy_obj(train_data_path)
            test_data = load_numpy_obj(test_data_path)

            x_train, y_train, x_test, y_test = (
                train_data[:, :-1],
                train_data[:, -1],
                test_data[:, :-1],
                test_data[:, -1]
            )

            # ------------------- Models -------------------
            models = {
                "Logistic Regression": LogisticRegression(),
                "KNN": KNeighborsClassifier(),
                "SVC": SVC(),
                "Decision Tree": DecisionTreeClassifier(),
                "Random Forest": RandomForestClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(),
                "AdaBoost": AdaBoostClassifier()
            }

            # ------------------- Hyperparameters -------------------
            params = {

                "Logistic Regression": {
                    "C": [0.01, 0.1, 1, 10],
                    "solver": ["lbfgs"],
                    "max_iter": [100, 200]
                },

                "KNN": {
                    "n_neighbors": [3, 5, 7],
                    "weights": ["uniform", "distance"]
                },

                "SVC": {
                    "C": [0.1, 1, 10],
                    "kernel": ["linear", "rbf"]
                },

                "Decision Tree": {
                    "criterion": ["gini", "entropy"],
                    "max_depth": [None, 10, 20]
                },

                "Random Forest": {
                    "n_estimators": [100, 200],
                    "max_depth": [None, 10, 20]
                },

                "Gradient Boosting": {
                    "n_estimators": [100, 200],
                    "learning_rate": [0.01, 0.1]
                },

                "AdaBoost": {
                    "n_estimators": [50, 100],
                    "learning_rate": [0.01, 0.1]
                }
            }

            # ------------------- Model Evaluation -------------------
            report, trained_models = self.evaluate_model(
                models, params, x_train, x_test, y_train, y_test
            )

            # ------------------- Best Model Selection -------------------
            best_model_name = max(report, key=report.get)
            best_model = trained_models[best_model_name]

            logging.info(f"Best Model Found: {best_model_name}")

            # ------------------- Predictions -------------------
            y_train_pred = best_model.predict(x_train)
            y_test_pred = best_model.predict(x_test)

            classification_train_matric = get_classification_matric(y_train, y_train_pred)
            classification_test_matric = get_classification_matric(y_test, y_test_pred)

            # ------------------- Save Model -------------------
            preprocessor_path = self.data_transformation_artifact.preprocessing_obj_path
            preprocessor = load_pickle_obj(preprocessor_path)

            training_model = TrainingModel(
                preprocessor=preprocessor,
                model=best_model
            )

            save_pickle_obj(
                obj=training_model,
                file_path=self.model_trainer_config.trained_model_path
            )

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_path=self.model_trainer_config.trained_model_path,
                train_classification_matric=classification_train_matric,
                test_classification_matric=classification_test_matric
            )

            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e, sys)
