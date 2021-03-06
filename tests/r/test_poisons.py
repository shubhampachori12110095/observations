from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.poisons import poisons


def test_poisons():
  """Test module poisons.py by downloading
   poisons.csv and testing shape of
   extracted data has 48 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = poisons(test_path)
  try:
    assert x_train.shape == (48, 3)
  except:
    shutil.rmtree(test_path)
    raise()
