{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM/e+QpS0E+zM1DqLd+tktf",
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
        "<a href=\"https://colab.research.google.com/github/johnrovan04-code/PYTHON-DS-LAB/blob/main/2)Insertion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SftnXLhxmEc6",
        "outputId": "a807e55c-2da0-483a-ad6c-a02600b5794e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 4 6 8 10 12 \n"
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
        "class CircularLinkedList:\n",
        "    def __init__(self):\n",
        "        self.last = None\n",
        "\n",
        "\n",
        "    def addToEmpty(self, data):\n",
        "        if self.last is not None:\n",
        "            return self.last\n",
        "\n",
        "        temp = Node(data)\n",
        "        self.last = temp\n",
        "        self.last.next = self.last\n",
        "\n",
        "        return self.last\n",
        "\n",
        "\n",
        "    def addBegin(self, data):\n",
        "        if self.last is None:\n",
        "            return self.addToEmpty(data)\n",
        "\n",
        "        temp = Node(data)\n",
        "        temp.next = self.last.next\n",
        "        self.last.next = temp\n",
        "\n",
        "        return self.last\n",
        "\n",
        "\n",
        "    def addEnd(self, data):\n",
        "        if self.last is None:\n",
        "            return self.addToEmpty(data)\n",
        "\n",
        "        temp = Node(data)\n",
        "        temp.next = self.last.next\n",
        "        self.last.next = temp\n",
        "        self.last = temp\n",
        "\n",
        "        return self.last\n",
        "\n",
        "\n",
        "    def addAfter(self, data, item):\n",
        "        if self.last is None:\n",
        "            return None\n",
        "\n",
        "        temp = Node(data)\n",
        "        p = self.last.next\n",
        "\n",
        "        while p:\n",
        "            if p.data == item:\n",
        "                temp.next = p.next\n",
        "                p.next = temp\n",
        "\n",
        "                if p == self.last:\n",
        "                    self.last = temp\n",
        "\n",
        "                return self.last\n",
        "\n",
        "            p = p.next\n",
        "\n",
        "            if p == self.last.next:\n",
        "                print(item, \"not present in the list\")\n",
        "                break\n",
        "\n",
        "        return self.last\n",
        "\n",
        "\n",
        "    def traverse(self):\n",
        "        if self.last is None:\n",
        "            print(\"List is empty\")\n",
        "            return\n",
        "\n",
        "        temp = self.last.next\n",
        "\n",
        "        while True:\n",
        "            print(temp.data, end=\" \")\n",
        "            temp = temp.next\n",
        "\n",
        "            if temp == self.last.next:\n",
        "                break\n",
        "\n",
        "        print()\n",
        "\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "\n",
        "    llist = CircularLinkedList()\n",
        "\n",
        "    last = llist.addToEmpty(6)\n",
        "    last = llist.addBegin(4)\n",
        "    last = llist.addBegin(2)\n",
        "    last = llist.addEnd(8)\n",
        "    last = llist.addEnd(12)\n",
        "    last = llist.addAfter(10, 8)\n",
        "\n",
        "    llist.traverse()"
      ]
    }
  ]
}