{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPxJziK9FEQQay8mABS3vK1",
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
        "<a href=\"https://colab.research.google.com/github/johnrovan04-code/PYTHON-DS-LAB/blob/main/2)Traversal.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PRoJv2zioaRx",
        "outputId": "d27cb732-e77e-4344-ff71-fe285557c066"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Contents of Circular Linked List:\n",
            "11 2 56 12 "
          ]
        }
      ],
      "source": [
        "class Node:\n",
        "\n",
        "    def __init__(self, data):\n",
        "        self.data = data\n",
        "        self.next = None\n",
        "\n",
        "\n",
        "class CircularLinkedList:\n",
        "\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "\n",
        "    def push(self, data):\n",
        "        ptr1 = Node(data)\n",
        "        temp = self.head\n",
        "\n",
        "        ptr1.next = self.head\n",
        "\n",
        "        if self.head is not None:\n",
        "\n",
        "            while temp.next != self.head:\n",
        "                temp = temp.next\n",
        "\n",
        "            temp.next = ptr1\n",
        "\n",
        "        else:\n",
        "            ptr1.next = ptr1\n",
        "\n",
        "        self.head = ptr1\n",
        "\n",
        "    def printList(self):\n",
        "        temp = self.head\n",
        "\n",
        "        if self.head is not None:\n",
        "\n",
        "            while True:\n",
        "                print(temp.data, end=\" \")\n",
        "                temp = temp.next\n",
        "\n",
        "                if temp == self.head:\n",
        "                    break\n",
        "\n",
        "\n",
        "\n",
        "cllist = CircularLinkedList()\n",
        "\n",
        "cllist.push(12)\n",
        "cllist.push(56)\n",
        "cllist.push(2)\n",
        "cllist.push(11)\n",
        "\n",
        "print(\"Contents of Circular Linked List:\")\n",
        "cllist.printList()"
      ]
    }
  ]
}