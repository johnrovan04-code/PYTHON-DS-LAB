{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPGQoTPGObk23Z8cZXF+x8a",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/johnrovan04-code/PYTHON-DS-LAB/blob/main/3)Traversal.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p7gFDZXprISF",
        "outputId": "39e856cd-99ce-414b-fdcd-c0d6f74031b0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Created DLL is:\n",
            "\n",
            "Traversal in forward direction\n",
            "1 7 8 6 4 \n",
            "Traversal in reverse direction\n",
            "4 6 8 7 1 \n"
          ]
        }
      ],
      "source": [
        "class Node:\n",
        "\n",
        "    def __init__(self, data):\n",
        "        self.data = data\n",
        "        self.next = None\n",
        "        self.prev = None\n",
        "\n",
        "\n",
        "class DoublyLinkedList:\n",
        "\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "\n",
        "    def push(self, new_data):\n",
        "        new_node = Node(new_data)\n",
        "\n",
        "        new_node.next = self.head\n",
        "\n",
        "        if self.head is not None:\n",
        "            self.head.prev = new_node\n",
        "\n",
        "        self.head = new_node\n",
        "\n",
        "    # Insert after a given node\n",
        "    def insertAfter(self, prev_node, new_data):\n",
        "\n",
        "        if prev_node is None:\n",
        "            print(\"The given previous node cannot be NULL\")\n",
        "            return\n",
        "\n",
        "        new_node = Node(new_data)\n",
        "\n",
        "        new_node.next = prev_node.next\n",
        "        prev_node.next = new_node\n",
        "\n",
        "        new_node.prev = prev_node\n",
        "\n",
        "        if new_node.next is not None:\n",
        "            new_node.next.prev = new_node\n",
        "\n",
        "    # Insert at end\n",
        "    def append(self, new_data):\n",
        "        new_node = Node(new_data)\n",
        "        new_node.next = None\n",
        "\n",
        "        if self.head is None:\n",
        "            new_node.prev = None\n",
        "            self.head = new_node\n",
        "            return\n",
        "\n",
        "        last = self.head\n",
        "\n",
        "        while last.next is not None:\n",
        "            last = last.next\n",
        "\n",
        "        last.next = new_node\n",
        "        new_node.prev = last\n",
        "\n",
        "    # Print forward and reverse\n",
        "    def printList(self, node):\n",
        "\n",
        "        print(\"\\nTraversal in forward direction\")\n",
        "\n",
        "        last = None\n",
        "\n",
        "        while node is not None:\n",
        "            print(node.data, end=\" \")\n",
        "            last = node\n",
        "            node = node.next\n",
        "\n",
        "        print(\"\\nTraversal in reverse direction\")\n",
        "\n",
        "        while last is not None:\n",
        "            print(last.data, end=\" \")\n",
        "            last = last.prev\n",
        "\n",
        "        print()\n",
        "\n",
        "\n",
        "\n",
        "llist = DoublyLinkedList()\n",
        "\n",
        "llist.append(6)\n",
        "llist.push(7)\n",
        "llist.push(1)\n",
        "llist.append(4)\n",
        "\n",
        "\n",
        "llist.insertAfter(llist.head.next, 8)\n",
        "\n",
        "print(\"Created DLL is:\")\n",
        "llist.printList(llist.head)"
      ]
    }
  ]
}