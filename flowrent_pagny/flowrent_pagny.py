"""
GROUP = dossa_d 994386

MEMBERS =
	dossa_d
	qasmi_m
	gueye_d
"""
from json import loads, dumps
from sys import argv
from hashlib import md5


class WorkFlowSimulation:
    """
    Provides tools to determine/simulate the execution of a given workflow

    Attributes
    ----------
    tasklist: list
    workflows: list
    simulatedWorkflows: list

    Methods
    -------
    getTask(int) -> dict

    getWorkflow(int) -> dict

    taskSimulator(task, input) -> bytes

    workFlowSimulation()
    """
    _PRIMITIVE = "primitive"
    _WORKFLOW = "workflow"
    tasklist: list
    workflows: list
    simulatedWorkflows: list = []

    def __init__(self, tasklist: list, workflows: list):
        self.tasklist = tasklist
        self.workflows = workflows

    def getTask(self, task_id: int) -> dict | None:
        """
        Returns a whole `task` from it's `id`.

        Parameters
        ----------
        task_id: int

        Returns
        -------
        task: (dict | None)
        """

        for task in self.tasklist:
            if task['id'] == task_id:
                return task

    def getWorkflow(self, workflow_id: int) -> dict | None:
        """
        Returns a `workflow` from it's `id`.

        Parameters
        ----------
        workflow_id: int

        Returns
        -------
        workflow: (dict | None)
        """

        for workflow in self.workflows:
            if workflow["workflow_id"] == workflow_id:
                return workflow

    def taskSimulator(self, task: dict, input: str) -> any:
        """
        Simulates a task. The use of the input of the calling workflow will occure only if the task is a primitive.

        Parameters
        ----------
        task: dict
        input: str

        Returns
        -------
        simulation: (Hash | None)
        """
        if task["task_type"] == self._PRIMITIVE:
            return md5(input.encode())
        elif task["task_type"] == self._WORKFLOW:
            simulation = b''
            for task_id in task["tasks"]:
                simulating = self.getTask(task_id)
                workflow = self.getWorkflow(task_id)
                simulation += self.taskSimulator(
                    simulating,
                    workflow["input"]
                    if workflow
                    else input
                ).digest()
            return md5(simulation)

        raise Exception("Task type unknown!")

    def workFlowSimulation(self) -> None:
        """
        Simulates the whole `workflows` list and fills the `simulatedWorkflows` list with the obtained values.

        Returns
        -------
            None
        """
        for workflow in self.workflows:
            self.simulatedWorkflows.append(
                self.taskSimulator(
                    self.getTask(workflow["workflow_id"]),
                    workflow["input"]
                ).hexdigest()
            )


if len(argv) >= 3:
    try:
        workflowSimulation = WorkFlowSimulation(loads(argv[1]), loads(argv[2]))
        workflowSimulation.workFlowSimulation()

        print(dumps(workflowSimulation.simulatedWorkflows))
    except Exception as e:
        print(e)
else:
    print("Try again with 2 arguments!")
