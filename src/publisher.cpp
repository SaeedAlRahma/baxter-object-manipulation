#include <Interface/SimulationGUI.h>
#include <IO/ROS.h>

int main(int argc,const char** argv) {

    // Create world
    RobotWorld world;
    SimGUIBackend backend(&world);
    WorldSimulation& sim = backend.sim;

    // Load world file
    if (!backend.LoadAndInitSim(argc,argv)) {
        cerr << "Error loading simulation from command line" << endl;
        return 1;
    }

    // Initialize ROS
    // This must be called before all other ROS calls
    if (!ROSInitialized()) {
        if (!ROSInit()) {
            cerr << "Error initializing ROS" << endl;
        }
        else {
            cout << "ROS initialized!" << endl;
        }
    }

    // Create subscriber and topic
    Robot robot_sub = *world.robots[0];     // dummy robot listener
    const char* topic = "myROSTopic";       // desired topic

    // Subscribe to joint state
    if (!ROSSubscribeJointState(robot_sub,topic)) {
        cerr << "Error subscribing joint state" << endl;
    }

    // Start simulation
    double dt = 0.1;
    while (sim.time < 3) {
        // Advance and update simulation
        sim.Advance(dt);
        sim.UpdateModel();
        cout << sim.time << ":\t";

        // Publish robot's joint state
        if (!ROSPublishJointState(*world.robots[0],topic)) {
          cerr << "Error publishing joint state" << endl;
        }

        // Check for updates
        if (ROSSubscribeUpdate()) {
            // robot_sub has now been updated from the topic
            cout << "Updated!" << endl;
        }
        else {
            // robot_sub already has the latest information
            cout << "No updates" << endl;
        }
    }

    // Print number of subscribed and published topics
    cout << "Subscribed to "<< ROSNumSubscribedTopics() << " topics" << endl;
    cout << "Published "<< ROSNumPublishedTopics() << " topics" << endl;

    // Shutdown ROS
    // Must call after all other ROS calls to cleanly shutdown ROS
    if (!ROSShutdown()) {
        cerr << "Error shutting down ROS" << endl;
    }

    return 0;
}

