from Graph import Graph
from error import errorPOPUP


def plot(self):
    try:
         function=self.expression.text()
         min_value=self.min_value.text()
         max_value=self.max_value.text()
         graph_plot = Graph(function,min_value,max_value)
    except ValueError as err:
        error_message = err.args[0]
        errorPOPUP(self, error_message)
        return

    self.graph.clear()
    self.graph.plot(graph_plot.x, graph_plot.y, pen="r")
