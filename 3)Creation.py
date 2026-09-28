{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOr5TxuxzQm+oCrRp1AUHmN",
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
        "<a href=\"https://colab.research.google.com/github/johnrovan04-code/PYTHON-DS-LAB/blob/main/3)Creation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kgzfpC4forG2",
        "outputId": "56b810df-35a1-4597-c944-eda1695636eb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Nodes of doubly linked list:\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "\n",
            "Count of nodes present in the list: 5\n"
          ]
        }
      ],
      "source": [
        "class Node:\n",
        "\n",
        "    def __init__(self, data):\n",
        "        self.data = data\n",
        "        self.previous = None\n",
        "        self.next = None\n",
        "\n",
        "\n",
        "class CountList:\n",
        "\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "        self.tail = None\n",
        "\n",
        "    def addNode(self, data):\n",
        "        newNode = Node(data)\n",
        "\n",
        "        if self.head is None:\n",
        "            self.head = self.tail = newNode\n",
        "            self.head.previous = None\n",
        "            self.tail.next = None\n",
        "\n",
        "        else:\n",
        "            self.tail.next = newNode\n",
        "            newNode.previous = self.tail\n",
        "            self.tail = newNode\n",
        "            self.tail.next = None\n",
        "\n",
        "    def countNodes(self):\n",
        "        counter = 0\n",
        "        current = self.head\n",
        "\n",
        "        while current is not None:\n",
        "            counter = counter + 1\n",
        "            current = current.next\n",
        "\n",
        "        return counter\n",
        "\n",
        "    def display(self):\n",
        "        current = self.head\n",
        "\n",
        "        if self.head is None:\n",
        "            print(\"List is empty\")\n",
        "            return\n",
        "\n",
        "        print(\"Nodes of doubly linked list:\")\n",
        "\n",
        "        while current is not None:\n",
        "            print(current.data)\n",
        "            current = current.next\n",
        "\n",
        "\n",
        "\n",
        "dList = CountList()\n",
        "\n",
        "dList.addNode(1)\n",
        "dList.addNode(2)\n",
        "dList.addNode(3)\n",
        "dList.addNode(4)\n",
        "dList.addNode(5)\n",
        "\n",
        "dList.display()\n",
        "\n",
        "print(\"\\nCount of nodes present in the list:\",\n",
        "      dList.countNodes())"
      ]
    }
  ]
}