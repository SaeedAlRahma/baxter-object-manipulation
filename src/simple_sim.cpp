#include <Interface/SimulationGUI.h>

int main(int argc,const char** argv) {
  //create a world
  RobotWorld world;

  //The SimGUIBackend class offers many helpers for setting
  //up default simulations, doing logging, sending paths, etc.
  //Advanced users may want to just create a WorldSimulation
  //class for more fine-grained control.
  SimGUIBackend backend(&world);
  WorldSimulation& sim=backend.sim;

  //If you have a fixed world that you want to use, you can
  //load any files like this
  //world.LoadElement("Klampt/data/robots/athlete.rob");
  //world.LoadElement("Klampt/data/terrains/plane.env");

  //Alternatively, this is helpful for loading command
  //line arguments like SimTest
  if(!backend.LoadAndInitSim(argc,argv)) {
    cerr<<"Error loading simulation from command line"<<endl;
    return 1;
  }

  //Uncomment+edit the following line to change the controller
  //time step for robot 0 (100Hz is the default)
  //sim.controlSimulators[0].controlTimeStep = 0.01;

  //Uncomment+edit the following line to change the underlying
  //simulation time step (1kHz is the default)
  //sim.simStep = 0.001;

  //pick some duration between printouts in main loop
  double dt = 0.1;
  //run the simulation
  while(sim.time < 5) {
    //** add control code here **

    //move the sim forward by the given time
    sim.Advance(dt);
    //update the world
    sim.UpdateModel();
    //print time, robot 0's configuration
    cout<<sim.time<<'\t'<<world.robots[0]->q<<endl;

    //Uncomment the following line to log the true state of
    //the robot to disk.
    //backend.DoStateLogging_LinearPath(0,"test_state.path");
  }
  return 0;
}
