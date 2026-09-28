{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNeUds9zDqXmJ4AV1t/FGOK",
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
        "<a href=\"https://colab.research.google.com/github/johnrovan04-code/PYTHON-DS-LAB/blob/main/2)creation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Al6Cc4Z2kWpD",
        "outputId": "01aa8385-07b1-47d7-aa41-73fc3c9b91b3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Nodes of the circular linked list:\n",
            "1\n",
            "2\n",
            "3\n",
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
        "class CreateList:\n",
        "    def __init__(self):\n",
        "        self.head = Node(None)\n",
        "        self.tail = Node(None)\n",
        "\n",
        "        self.head.next = self.tail\n",
        "        self.tail.next = self.tail\n",
        "\n",
        "    def add(self, data):\n",
        "        new_Node = Node(data)\n",
        "\n",
        "        if self.head.data is None:\n",
        "            self.head = new_Node\n",
        "            self.tail = new_Node\n",
        "            new_Node.next = self.head\n",
        "        else:\n",
        "            self.tail.next = new_Node\n",
        "            self.tail = new_Node\n",
        "            self.tail.next = self.head\n",
        "\n",
        "    def display(self):\n",
        "        if self.head.data is None:\n",
        "            print(\"List is empty\")\n",
        "            return\n",
        "\n",
        "        current = self.head\n",
        "\n",
        "        print(\"Nodes of the circular linked list:\")\n",
        "\n",
        "        while True:\n",
        "            print(current.data)\n",
        "            current = current.next\n",
        "\n",
        "            if current == self.head:\n",
        "                break\n",
        "\n",
        "\n",
        "c1 = CreateList()\n",
        "c1.add(1)\n",
        "c1.add(2)\n",
        "c1.add(3)\n",
        "c1.add(4)\n",
        "\n",
        "c1.display()\n"
      ]
    }
  ]
}