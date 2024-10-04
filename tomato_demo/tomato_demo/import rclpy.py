import rclpy
from rclpy.node import Node
from std_mags.msg import String

class Responder(Node):
    def __init__(self):
        super().__init__('pose_publisher')
        self.sub = self.create_subscription(String, '/base_msg', self.msg_callback)
        self.pub = self.create_publisher(String, '/ex_msg', 10)


def main():



if__name__ == '__main__':
    main()