{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNtnI3LcPzxQ5GhrZKjbKBy",
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
        "<a href=\"https://colab.research.google.com/github/johnrovan04-code/PYTHON-DS-LAB/blob/main/3)Insertion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q631TA-sqhcM",
        "outputId": "82e6e436-2a31-462b-d70a-7ecabb7e5438"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Adding a node to the start of the list:\n",
            "1\n",
            "\n",
            "Adding a node to the start of the list:\n",
            "2\n",
            "1\n",
            "\n",
            "Adding a node to the start of the list:\n",
            "3\n",
            "2\n",
            "1\n",
            "\n",
            "Adding a node to the start of the list:\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n",
            "\n",
            "Adding a node to the start of the list:\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n",
            "\n"
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
        "class InsertStart:\n",
        "\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "        self.tail = None\n",
        "\n",
        "    def addAtStart(self, data):\n",
        "        newNode = Node(data)\n",
        "\n",
        "        if self.head is None:\n",
        "            self.head = self.tail = newNode\n",
        "            self.head.previous = None\n",
        "            self.tail.next = None\n",
        "\n",
        "        else:\n",
        "            self.head.previous = newNode\n",
        "            newNode.next = self.head\n",
        "            newNode.previous = None\n",
        "            self.head = newNode\n",
        "\n",
        "    def display(self):\n",
        "        current = self.head\n",
        "\n",
        "        if self.head is None:\n",
        "            print(\"List is empty\")\n",
        "            return\n",
        "\n",
        "        print(\"Adding a node to the start of the list:\")\n",
        "\n",
        "        while current is not None:\n",
        "            print(current.data)\n",
        "            current = current.next\n",
        "\n",
        "        print()\n",
        "\n",
        "\n",
        "dList = InsertStart()\n",
        "\n",
        "dList.addAtStart(1)\n",
        "dList.display()\n",
        "\n",
        "dList.addAtStart(2)\n",
        "dList.display()\n",
        "\n",
        "dList.addAtStart(3)\n",
        "dList.display()\n",
        "\n",
        "dList.addAtStart(4)\n",
        "dList.display()\n",
        "\n",
        "dList.addAtStart(5)\n",
        "dList.display()"
      ]
    }
  ]
}