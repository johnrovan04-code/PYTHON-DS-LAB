{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM19mrs2zP4CLMt8a3DLYPy",
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
        "<a href=\"https://colab.research.google.com/github/johnrovan04-code/PYTHON-DS-LAB/blob/main/3)Deletion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IZehQTTDqMjd",
        "outputId": "f79df29d-6c4f-4bba-a4f9-1680e53f0012"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original List:\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "\n",
            "Updated List:\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "\n",
            "Updated List:\n",
            "3\n",
            "4\n",
            "5\n",
            "\n",
            "Updated List:\n",
            "4\n",
            "5\n",
            "\n",
            "Updated List:\n",
            "5\n",
            "\n",
            "Updated List:\n",
            "List is empty\n"
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
        "class DeleteStart:\n",
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
        "    def deleteFromStart(self):\n",
        "\n",
        "        if self.head is None:\n",
        "            return\n",
        "\n",
        "        else:\n",
        "\n",
        "            if self.head != self.tail:\n",
        "                self.head = self.head.next\n",
        "                self.head.previous = None\n",
        "\n",
        "            else:\n",
        "                self.head = self.tail = None\n",
        "\n",
        "    def display(self):\n",
        "        current = self.head\n",
        "\n",
        "        if self.head is None:\n",
        "            print(\"List is empty\")\n",
        "            return\n",
        "\n",
        "        while current is not None:\n",
        "            print(current.data)\n",
        "            current = current.next\n",
        "\n",
        "        print()\n",
        "\n",
        "dList = DeleteStart()\n",
        "\n",
        "dList.addNode(1)\n",
        "dList.addNode(2)\n",
        "dList.addNode(3)\n",
        "dList.addNode(4)\n",
        "dList.addNode(5)\n",
        "\n",
        "print(\"Original List:\")\n",
        "dList.display()\n",
        "\n",
        "while dList.head is not None:\n",
        "    dList.deleteFromStart()\n",
        "    print(\"Updated List:\")\n",
        "    dList.display()"
      ]
    }
  ]
}