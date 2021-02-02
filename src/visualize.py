import time

import matplotlib.pyplot as plt
import networkx as nx

from data_classes import Shape


class Visualize:

    __graph = nx.Graph()

    @staticmethod
    def __add_node_to_graph(graph, position):
        graph.add_node(position)

    @staticmethod
    def __add_edge_to_graph(graph, u, v):
        graph.add_edge(u, v)

    @staticmethod
    def __get_filled_nodes(board):
        filled_positions = []
        for i in range(board.size):
            for j in range(board.size):
                if board[i][j] == 1:
                    filled_positions.append((i, j))
        return filled_positions

    @staticmethod
    def __get_empty_nodes(board):
        empty_positions = []
        for i in range(board.size):
            for j in range(board.size):
                if board[i][j] == 0:
                    empty_positions.append((i, j))
        return empty_positions

    @staticmethod
    def __get_legal_positions(board):
        legal_positions = []
        for i in range(board.size):
            for j in range(board.size):
                if board[i][j] is None:
                    legal_positions.append((i, j))
        return legal_positions

    @classmethod
    def initialize_board(cls, board, edges, board_type):
        cls.__graph = nx.Graph()
        size = board.size

        legal_positions = Visualize.__get_legal_positions(board)

        # Creates a Hex Diamon grid
        if board_type == Shape.Diamond:
            for i in range(size):
                for j in range(size):
                    Visualize.__add_node_to_graph(Visualize.__graph, (i, j))

        # Create a Hex Triangle grid
        elif board_type == Shape.Triangle:
            for i in range(size):
                for j in range(i + 1):
                    Visualize.__add_node_to_graph(Visualize.__graph, (i, j))

        for x, y in legal_positions:
            for row_offset, column_offset in edges:
                neighbor_node = (x + row_offset, y + column_offset)
                if neighbor_node in legal_positions:
                    Visualize.__add_edge_to_graph(Visualize.__graph, (x, y), neighbor_node)

    @staticmethod
    def draw_board(board_type, board, action_nodes, delay):

        # List of all node positions currently filled
        filled_nodes = Visualize.__get_filled_nodes(board)
        empty_nodes = Visualize.__get_empty_nodes(board)
        legal_positions = Visualize.__get_legal_positions(board)
        size = board.size
        positions = {}

        # Position nodes to shape a Triangle
        if board_type == Shape.Triangle:
            for node in legal_positions:
                positions[node] = (2 * node[1] - node[0], size - node[0])

        # Position nodes to shape a Diamond
        elif board_type == Shape.Diamond:
            for node in legal_positions:
                positions[node] = ((node[1] - node[0]), (size - node[1] - node[0]))

        # Remove nodes currently active
        for nodes in action_nodes:
            filled_nodes.remove(nodes)

        # Draw the resulting grid
        nx.draw_networkx_nodes(Visualize.__graph, positions, nodelist=empty_nodes, node_color='black')
        nx.draw_networkx_nodes(Visualize.__graph, positions, nodelist=filled_nodes, node_color='blue')
        nx.draw_networkx_nodes(Visualize.__graph, positions, nodelist=action_nodes[0], node_color='green')
        nx.draw_networkx_nodes(Visualize.__graph, positions, nodelist=action_nodes[1], node_color='red')
        nx.draw_networkx_edges(Visualize.__graph, positions, width=1)

        # Takes in delay for each move. Delay given in seconds
        time.sleep(delay * 1000)

        plt.axis('off')
        plt.draw()
        plt.clf()
        plt.show()

    @staticmethod
    def plot_training_data(training_data):
        plt.title('Training data')
        plt.xlabel('Episode')
        plt.ylabel('Remaining Pegs')

        plt.plot(training_data, color='tab:blue')

        plt.tight_layout()
        plt.savefig('src/results/training_data.png')
        plt.close()
