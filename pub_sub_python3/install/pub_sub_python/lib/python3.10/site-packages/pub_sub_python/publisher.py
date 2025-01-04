import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class NodePublisher(Node):
    def __init__(self):
        super().__init__('node_publisher')
        self.publisher_ = self.create_publisher(String, 'communication_topic', 15)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.callbackFunction)
        self.counter=0
        
    def callbackFunction(self):
        msg = String()
        msg.data = "counter value: %d" % self.counter
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publisher Node is Publishing: %s" % msg.data)
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node_publisher = NodePublisher()
    
    try:
        rclpy.spin(node_publisher)
    except KeyboardInterrupt:
        pass
    
    node_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
