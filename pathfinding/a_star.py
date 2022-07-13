"""
A* pathfinding algorithm
Implementation taken from Ryan Collingwood in astar.py
https://gist.github.com/ryancollingwood/32446307e976a11a1185a5394d6657bc
"""

from array import array
import heapq
from xml.dom import NodeFilter


class Node:
    """
    Node class for A* pathfinding algorithm
    """

    def __init__(self, parent: "Node"=None, position: tuple=None) -> None:
        self.parent = parent  # Another Node class
        self.position = position  # This should be a tuple of (x, y)
        ## Effects of the node ##
        # f = Total cost of a node
        # g = Distance between current node and start node
        # h = Heuristic; estimated distance from current node to end node
        self.f = 0  
        self.g = 0  
        self.h = 0  

    def __eq__(self, other: "Node") -> None:
        """Test if two nodes are the same"""
        return self.position == other.position

    def __repr__(self) -> None:
        """Get representation of a node"""
        return f"{self.position} - f: {self.f}, g: {self.g}, h: {self.h}"

    def __lt__(self, other: "Node") -> None:
        """Redefine less than operator for purposes of heap queue"""
        return self.f < other.f

    def __gt__(self, other: "Node") -> None:
        """Redefine greater than operator for purposes of heap queue"""
        return self.f > other.f


def return_path(current_node: Node) -> list:
    """
    Return path of A* algorithm to get from start to end node
    """
    path = []
    current = current_node
    # Continually iterate through nodes until entire path is elucidated
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Iterate through list backward to return reversed path


def Astar(area: array, start: Node, end: Node) -> list:
    """
    A* pathfinding algorithm
    :param area:
    :param start: (Node) Tuple of starting position
    :param end: (Node) Tuple of ending position
    :return: List of tuples as a path from start node to end node in area
    """
    # Convert start and end nodes to be viable options
    area[start.position[0]][start.position[1]] = 0.
    area[end.position[0]][end.position[1]] = 0.
    # Initialize available and unavailable list of nodes
    available, unavailable = [], []
    # Heapify the list of available nodes and add the start node
    heapq.heapify(available) # heapq library implements heap queue algorithm for searching a list
    heapq.heappush(available, start)
    # Create termination condition
    current_iterations, max_iterations = 0, (len(area[0]) * len(area) // 2)
    # Set which squares we're going to search
    # This allows for diagonal moves
    adjacent = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))

    # Loop until we find the end
    while current_iterations <= max_iterations:
        current_iterations += 1
        # Get current node and move it from available list to unavailable list
        current_node = heapq.heappop(available)
        unavailable.append(current_node)
        # Test if current node is the end node. If so, get outta there
        if current_node == end:
            return return_path(current_node)
        # Otherwise, proceed with algorithm
        # Firstly, generate daughter nodes
        daughters = []
        for candidate in adjacent:
            # Get node position
            # 1. Ensure that the candidate node is node is not off the board
            # 2. Ensure that the candidate node is not occupied by a piece
            candidate_node = (current_node.position[0] + candidate[0], current_node.position[1] + candidate[1])
            if (
                    candidate_node[0] > (len(area) - 1) or
                    candidate_node[0] < 0 or
                    candidate_node[1] > (len(area[len(area) - 1]) - 1) or
                    candidate_node[1] < 0
            ) or area[candidate_node[0]][candidate_node[1]] != 0.0:
                continue

            # If all of the above is true, we can create and append this new node to the current path
            daughters.append(Node(current_node, candidate_node))
        # Now we loop through all of the daughter nodes to find the optimal path
        for girl in daughters:
            # First make sure that girl is on the list of nodes traveled
            if len([closed_girl for closed_girl in unavailable if closed_girl == girl]) > 0:
                continue
            # Create f, g, and h values
            girl.g = current_node.g + 1
            girl.h = ((girl.position[0] - end.position[0]) ** 2) + ((girl.position[1] - end.position[1]) ** 2)
            girl.f = girl.g + girl.h
            # Check if girl is already in open list
            if len([open_node for open_node in available if
                    girl.position == open_node.position and girl.g > open_node.g]) > 0:
                continue
            # Add girl to open list
            heapq.heappush(available, girl)

    return None  # return None if no path is ever found between start and end
