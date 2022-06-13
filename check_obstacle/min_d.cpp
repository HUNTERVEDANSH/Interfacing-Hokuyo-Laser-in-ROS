void LeftClosestObstacle::messageCallback(const sensor_msgs::LaserScan::ConstPtr &msg) {
    int size = msg->ranges.size();
    int minIndex = 0;
    int maxIndex = 540; //0 to 540 for left side minimum distance
    int closestIndex = -1;
    double minVal = 999; //values are between 0.2 and 30 meters for my scanner

    for (int i = minIndex; i < maxIndex; i++)
    {
        if ((msg->ranges[i] <= minVal) && (msg->ranges[i] >= msg->range_min) && (msg->ranges[i] <= msg->range_max))
        {
            minVal = msg->ranges[i];
            closestIndex = i;
        }
    }
    ROS_INFO_STREAM("Min ---" << msg->ranges[closestIndex]); }kv
