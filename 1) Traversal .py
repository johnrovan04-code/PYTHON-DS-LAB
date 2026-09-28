{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPyt5SMCm1bpWIvY/sR/Tqb",
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
        "<a href=\"https://colab.research.google.com/github/johnrovan04-code/PYTHON-DS-LAB/blob/main/1)%20Traversal%20.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "  def __init__(self,data):\n",
        "    self.data=data\n",
        "    self.next=None\n",
        "class LinkedList:\n",
        "  def __init__(self):\n",
        "    self.head=None\n",
        "  def printList(self):\n",
        "    temp=self.head\n",
        "    while(temp):\n",
        "      print(temp.data)\n",
        "      temp=temp.next\n",
        "if __name__==\"__main__\":\n",
        "  llist=LinkedList()\n",
        "\n",
        "  llist.head=Node(1)\n",
        "  second=Node(2)\n",
        "  third=Node(3)\n",
        "\n",
        "  llist.head.next=second\n",
        "  second.next=third\n",
        "\n",
        "  llist.printList()\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GtLYCdt3jgac",
        "outputId": "99442e3a-7f67-466b-a9ef-bf5ae20cd269"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n"
          ]
        }
      ]
    }
  ]
}