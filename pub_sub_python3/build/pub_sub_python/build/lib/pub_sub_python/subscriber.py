import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class NodeSubscriber(Node):
    def __init__(self):
        super().__init__('node_subscriber')
        self.subscription = self.create_subscription(
            String,
            'communication_topic',
            self.callbackFunction,
            15)

        self.subscription  # prevent unused variable warning
        
    def callbackFunction(self, msg):
        self.get_logger().info(f"Subscriber Node Received: %s" %msg.data)

def main(args=None):
    rclpy.init(args=args)
    random_number_subscriber = NodeSubscriber()
    
    try:
        rclpy.spin(random_number_subscriber)
    except KeyboardInterrupt:
        pass
    
    random_number_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
