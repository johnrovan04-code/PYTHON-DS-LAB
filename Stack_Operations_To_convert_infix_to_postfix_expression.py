{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNiRhN9GGN+pwl0d9RpbTKK",
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
        "<a href=\"https://colab.research.google.com/github/johnrovan04-code/PYTHON-DS-LAB/blob/main/Stack_Operations_To_convert_infix_to_postfix_expression.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r3MRi_kx-bU6",
        "outputId": "806f219e-e450-4627-92e5-1ec0392d4749"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Postfix expression: abcd^e-fgh*+^*+i-\n"
          ]
        }
      ],
      "source": [
        "class Conversion:\n",
        "\n",
        "    def __init__(self, capacity):\n",
        "        self.top = -1\n",
        "        self.capacity = capacity\n",
        "        self.array = []\n",
        "        self.output = []\n",
        "\n",
        "        self.precedence = {\n",
        "            '+': 1,\n",
        "            '-': 1,\n",
        "            '*': 2,\n",
        "            '/': 2,\n",
        "            '^': 3\n",
        "        }\n",
        "\n",
        "    def isEmpty(self):\n",
        "        return True if self.top == -1 else False\n",
        "\n",
        "    def peek(self):\n",
        "        return self.array[-1]\n",
        "\n",
        "    def pop(self):\n",
        "        if not self.isEmpty():\n",
        "            self.top -= 1\n",
        "            return self.array.pop()\n",
        "        else:\n",
        "            return \"$\"\n",
        "\n",
        "    def push(self, op):\n",
        "        self.top += 1\n",
        "        self.array.append(op)\n",
        "\n",
        "    def isOperand(self, ch):\n",
        "        return ch.isalpha()\n",
        "\n",
        "    def notGreater(self, i):\n",
        "        try:\n",
        "            a = self.precedence[i]\n",
        "            b = self.precedence[self.peek()]\n",
        "\n",
        "            return True if a <= b else False\n",
        "\n",
        "        except KeyError:\n",
        "            return False\n",
        "\n",
        "    def infixToPostfix(self, exp):\n",
        "\n",
        "        for i in exp:\n",
        "\n",
        "            if self.isOperand(i):\n",
        "                self.output.append(i)\n",
        "\n",
        "\n",
        "            elif i == '(':\n",
        "                self.push(i)\n",
        "\n",
        "            # If closing parenthesis\n",
        "            elif i == ')':\n",
        "\n",
        "                while not self.isEmpty() and self.peek() != '(':\n",
        "                    a = self.pop()\n",
        "                    self.output.append(a)\n",
        "\n",
        "                if not self.isEmpty() and self.peek() == '(':\n",
        "                    self.pop()\n",
        "                else:\n",
        "                    return -1\n",
        "\n",
        "            # If operator\n",
        "            else:\n",
        "\n",
        "                while (\n",
        "                    not self.isEmpty()\n",
        "                    and self.notGreater(i)\n",
        "                ):\n",
        "                    self.output.append(self.pop())\n",
        "\n",
        "                self.push(i)\n",
        "\n",
        "        while not self.isEmpty():\n",
        "            self.output.append(self.pop())\n",
        "\n",
        "        print(\"Postfix expression:\", \"\".join(self.output))\n",
        "\n",
        "\n",
        "\n",
        "exp = \"a+b*(c^d-e)^(f+g*h)-i\"\n",
        "\n",
        "obj = Conversion(len(exp))\n",
        "\n",
        "obj.infixToPostfix(exp)"
      ]
    }
  ]
}