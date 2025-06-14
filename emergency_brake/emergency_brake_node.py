import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class EmergencyBrakeNode(Node):

    def __init__(self):
        super().__init__('emergency_brake_node')
        self.declare_parameter('braking_distance', 1.0)  # Default braking distance = 1m

        self.scan_sub = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.get_logger().info('🚨 Emergency Brake Node Started')

    def scan_callback(self, msg):
        braking_distance = self.get_parameter('braking_distance').value
        min_distance = min(msg.ranges)

        if min_distance < braking_distance:
            self.apply_brake()
            self.get_logger().warn(f'🚨 Obstacle at {min_distance:.2f}m! Applying Emergency Brake.')

    def apply_brake(self):
        stop_msg = Twist()
        stop_msg.linear.x = 0.0
        stop_msg.angular.z = 0.0
        self.cmd_vel_pub.publish(stop_msg)

def main(args=None):
    rclpy.init(args=args)
    node = EmergencyBrakeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()