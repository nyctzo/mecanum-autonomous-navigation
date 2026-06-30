#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "std_msgs/msg/float64.hpp"

class MecanumControlNode : public rclcpp::Node
{
public:
    MecanumControlNode()
    : Node("mecanum_control_node")
    {
        cmd_vel_sub_ = this->create_subscription<geometry_msgs::msg::Twist>(
            "/cmd_vel",
            10,
            std::bind(&MecanumControlNode::cmdVelCallback,
                      this,
                      std::placeholders::_1));

        fl_pub_ = this->create_publisher<std_msgs::msg::Float64>(
            "/front_left_wheel_velocity", 10);

        fr_pub_ = this->create_publisher<std_msgs::msg::Float64>(
            "/front_right_wheel_velocity", 10);

        rl_pub_ = this->create_publisher<std_msgs::msg::Float64>(
            "/rear_left_wheel_velocity", 10);

        rr_pub_ = this->create_publisher<std_msgs::msg::Float64>(
            "/rear_right_wheel_velocity", 10);

        RCLCPP_INFO(this->get_logger(), "Mecanum Control Node Started");
    }

private:
    void cmdVelCallback(const geometry_msgs::msg::Twist::SharedPtr msg)
    {
        // Desired robot velocity
        const double vx = msg->linear.x;
        const double vy = msg->linear.y;
        const double wz = msg->angular.z;

        // Robot dimensions
        const double wheel_radius = 0.06;      // meters
        const double robot_length = 0.445;     // meters
        const double robot_width  = 0.30;      // meters

        const double L = robot_length / 2.0;
        const double W = robot_width / 2.0;

        // Inverse kinematics
        const double front_left =
            (vx - vy - (L + W) * wz) / wheel_radius;

        const double front_right =
            (vx + vy + (L + W) * wz) / wheel_radius;

        const double rear_left =
            (vx + vy - (L + W) * wz) / wheel_radius;

        const double rear_right =
            (vx - vy + (L + W) * wz) / wheel_radius;

        // Publish wheel velocities
        std_msgs::msg::Float64 fl_msg;
        std_msgs::msg::Float64 fr_msg;
        std_msgs::msg::Float64 rl_msg;
        std_msgs::msg::Float64 rr_msg;

        fl_msg.data = front_left;
        fr_msg.data = front_right;
        rl_msg.data = rear_left;
        rr_msg.data = rear_right;

        fl_pub_->publish(fl_msg);
        fr_pub_->publish(fr_msg);
        rl_pub_->publish(rl_msg);
        rr_pub_->publish(rr_msg);

        // Console output
        RCLCPP_INFO(
            this->get_logger(),
            "\n"
            "====================================\n"
            "Robot Velocity\n"
            "vx : %.2f m/s\n"
            "vy : %.2f m/s\n"
            "wz : %.2f rad/s\n"
            "\n"
            "Wheel Angular Velocities\n"
            "Front Left  : %.2f rad/s\n"
            "Front Right : %.2f rad/s\n"
            "Rear Left   : %.2f rad/s\n"
            "Rear Right  : %.2f rad/s\n"
            "====================================",
            vx,
            vy,
            wz,
            front_left,
            front_right,
            rear_left,
            rear_right);
    }

    rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr cmd_vel_sub_;

    rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr fl_pub_;
    rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr fr_pub_;
    rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr rl_pub_;
    rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr rr_pub_;
};

int main(int argc, char ** argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MecanumControlNode>());
    rclcpp::shutdown();
    return 0;
}
