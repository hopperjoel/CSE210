from game.action import Action

class DrawActorsAction(Action):
    """A code template for drawing all actors.

    Stereotype: Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService"""

    def __init__(self, output_service):
        """This is the class constructor.

        Args:
            _output_service (OutputService): An instance of OutputService
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            _output_service (OutputService): An instance of OutputService
        """
        self._output_service.clear_screen()
        artifacts = cast["artifact"]
        robot = cast["robot"][0]
        marquee = cast["marquee"][0]
        actors_list = [robot, marquee]
        self._output_service.draw_actors(artifacts)
        self._output_service.draw_actors(actors_list)
        self._output_service.flush_buffer()