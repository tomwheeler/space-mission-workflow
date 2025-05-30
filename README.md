# space-mission-workflow
Example workflow based on a space mission theme

# Setup

First, create a virtual environment.

```bash
python -m venv env
```

Next, activate that environment. 

```bash
source env/bin/activate
```

Install the Temporal Python SDK.

```bash
pip install temporalio
```

# Running the example
Start the Temporal Service (if it's not already running).

```bash
temporal server start-dev
```

Next, start the Worker.

```bash
python worker.py
```

Open another terminal, activate the virtual environment there, and 
then run the program to start the Workflow Execution.

```bash
source env/bin/activate
python starter.py
```

You should now go to the Web UI to see what's already happened. After 
the launch sequence (a ten-second count), the spaceship will begin 
collecting data by using an Activity to read measurements from its
probe. It will repeat this every 5 minutes until it's signalled to 
return back home to earth.

You can use a Query to see the mission's status at any time.

```bash
temporal workflow query --workflow-id launch-space-mission-001 --name get_status
```

When you'd like to call the spaceship back to earth, run this command 
to send the Signal. This will complete the Workflow Execution.

```bash
temporal workflow signal --workflow-id launch-space-mission-001 --name initiate_return
```



