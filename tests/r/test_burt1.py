from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.burt1 import burt1


def test_burt1():
  """Test module burt1.py by downloading
   burt1.csv and testing shape of
   extracted data has 11 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = burt1(test_path)
  try:
    assert x_train.shape == (11, 11)
  except:
    shutil.rmtree(test_path)
    raise()
