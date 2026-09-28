{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP9gTmOXIGsrWwcKU248jud",
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
        "<a href=\"https://colab.research.google.com/github/johnrovan04-code/PYTHON-DS-LAB/blob/main/1)deletion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sHID56P5gG-9",
        "outputId": "92acb7c1-c521-4a71-a85c-7e2c6f32395c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Created linked list is:\n",
            "1\n",
            "7\n",
            "8\n",
            "6\n",
            "4\n"
          ]
        }
      ],
      "source": [
        "class Node:\n",
        "    def __init__(self, data):\n",
        "        self.data = data\n",
        "        self.next = None\n",
        "\n",
        "\n",
        "class LinkedList:\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "\n",
        "    def push(self, new_data):\n",
        "        new_node = Node(new_data)\n",
        "        new_node.next = self.head\n",
        "        self.head = new_node\n",
        "\n",
        "    def insertAfter(self, prev_node, new_data):\n",
        "        if prev_node is None:\n",
        "            print(\"The given previous node must be in LinkedList.\")\n",
        "            return\n",
        "\n",
        "        new_node = Node(new_data)\n",
        "        new_node.next = prev_node.next\n",
        "        prev_node.next = new_node\n",
        "\n",
        "    def append(self, new_data):\n",
        "        new_node = Node(new_data)\n",
        "\n",
        "        if self.head is None:\n",
        "            self.head = new_node\n",
        "            return\n",
        "\n",
        "        last = self.head\n",
        "\n",
        "        while last.next:\n",
        "            last = last.next\n",
        "\n",
        "        last.next = new_node\n",
        "\n",
        "    def printList(self):\n",
        "        temp = self.head\n",
        "\n",
        "        while temp:\n",
        "            print(temp.data)\n",
        "            temp = temp.next\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    llist = LinkedList()\n",
        "\n",
        "    llist.push(6)\n",
        "    llist.push(7)\n",
        "    llist.push(1)\n",
        "    llist.append(4)\n",
        "    llist.insertAfter(llist.head.next, 8)\n",
        "\n",
        "    print(\"Created linked list is:\")\n",
        "    llist.printList()\n"
      ]
    }
  ]
}