package org.apache.spark.h2o.utils

import com.github.sakserv.minicluster.impl.YarnLocalCluster


/**
  * Created by kuba on 20/03/2017.
  */
trait MiniYarnClusterSupport {
  def start() {
    val yarnLocalCluster = new YarnLocalCluster.Builder()
      .setNumNodeManagers(1)
      .setNumLocalDirs(1)
        .setNumLogDirs(1)
          .setResourceManagerAddress("localhost:37001")
          .setResourceManagerHostname("localhost")
          .setResourceManagerSchedulerAddress("localhost:37002")
          .setResourceManagerResourceTrackerAddress("localhost:37003")
          .setResourceManagerWebappAddress("localhost:37004")
          .setUseInJvmContainerExecutor(false)
          .build()

    yarnLocalCluster.start()
  }
}
