{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN1ju9ll7ov9/jJ48mYwDOJ",
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
        "<a href=\"https://colab.research.google.com/github/johnrovan04-code/PYTHON-DS-LAB/blob/main/2)Deletion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2Hnu9Qk9k4OS",
        "outputId": "a38bb5be-5deb-4120-b172-40f5f83cf88a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original List:\n",
            "1 2 3 4 \n",
            "Updated List:\n",
            "1 2 3 \n",
            "Updated List:\n",
            "1 2 \n",
            "Updated List:\n",
            "1 \n",
            "Updated List:\n",
            "List is empty\n"
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
        "        self.head = None\n",
        "        self.tail = None\n",
        "\n",
        "\n",
        "    def add(self, data):\n",
        "        newNode = Node(data)\n",
        "\n",
        "        if self.head is None:\n",
        "            self.head = newNode\n",
        "            self.tail = newNode\n",
        "            newNode.next = self.head\n",
        "        else:\n",
        "            self.tail.next = newNode\n",
        "            self.tail = newNode\n",
        "            self.tail.next = self.head\n",
        "\n",
        "\n",
        "    def deleteEnd(self):\n",
        "        if self.head is None:\n",
        "            return\n",
        "\n",
        "\n",
        "        if self.head == self.tail:\n",
        "            self.head = None\n",
        "            self.tail = None\n",
        "            return\n",
        "\n",
        "        current = self.head\n",
        "\n",
        "\n",
        "        while current.next != self.tail:\n",
        "            current = current.next\n",
        "\n",
        "        self.tail = current\n",
        "        self.tail.next = self.head\n",
        "\n",
        "\n",
        "    def display(self):\n",
        "        if self.head is None:\n",
        "            print(\"List is empty\")\n",
        "            return\n",
        "\n",
        "        current = self.head\n",
        "\n",
        "        while True:\n",
        "            print(current.data, end=\" \")\n",
        "            current = current.next\n",
        "\n",
        "            if current == self.head:\n",
        "                break\n",
        "\n",
        "        print()\n",
        "\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "\n",
        "    cl = CreateList()\n",
        "\n",
        "    cl.add(1)\n",
        "    cl.add(2)\n",
        "    cl.add(3)\n",
        "    cl.add(4)\n",
        "\n",
        "    print(\"Original List:\")\n",
        "    cl.display()\n",
        "\n",
        "    while cl.head is not None:\n",
        "        cl.deleteEnd()\n",
        "\n",
        "        print(\"Updated List:\")\n",
        "        cl.display()"
      ]
    }
  ]
}