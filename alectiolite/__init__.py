from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import os
import sys
import random
import logging
import alectiolite

from .init import init_experiment_ 
from .curate.classification import UniClassification as curate_classification

__all__ = ['backend',
           'curate',
           'proto',
           'callbacks'
           'init_experiment_',
           'UniClassification']







init = alectiolite.init_experiment_
curate_classification = alectiolite.curate_classification