import logging
import os

from rasa_core import utils, train
from rasa_core.agent import Agent
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer, LabelTokenizerSingleStateFeaturizer,FullDialogueTrackerFeaturizer
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy, AugmentedMemoizationPolicy

logger = logging.getLogger(__name__)

utils.configure_colored_logging(loglevel='DEBUG')


def train_dialogue(domain_file,
                   model_path,
                   training_folder,
                   policy_config):
    return train.train_dialogue_model(domain_file=domain_file,
                                      stories_file=training_folder,
                                      output_path=model_path,
                                      policy_config=policy_config,
                                      kwargs={'augmentation_factor': 20,
                                              'validation_split': 0.2,}
                                      )

if __name__ == "__main__":
    train_dialogue('domain.yml', 'models/dialogue', 'data/stories/', 'policy_config.yml')
