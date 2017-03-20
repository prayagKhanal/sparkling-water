#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Unit tests for PySparkling Conf class;
"""

import unittest
from pysparkling.context import H2OContext
from pysparkling.conf import H2OConf
from pyspark import SparkContext, SparkConf

import h2o
import test_utils


class H2OConfTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._sc = SparkContext(conf=test_utils.get_default_spark_conf().set("spark.ext.h2o.cloud.name", "test-cloud"))
        test_utils.set_up_class(cls)
        h2o_conf = H2OConf(cls._sc).set_num_of_external_h2o_nodes(2)
        cls._hc = H2OContext.getOrCreate(cls._sc, h2o_conf)

    @classmethod
    def tearDownClass(cls):
        test_utils.tear_down_class(cls)

    # test passing h2o_conf to H2OContext
    def test_h2o_conf(self):
        self.assertEquals(self._hc.get_conf().cloud_name(), "test-cloud",
                          "Configuration property cloud_name should match")


if __name__ == '__main__':
    test_utils.run_tests([H2OConfTest], file_name="py_unit_tests_conf")
