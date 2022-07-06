{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "calculo de media",
      "provenance": [],
      "authorship_tag": "ABX9TyPKppSIJPU1Lr5oEUoMaX9a",
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
        "<a href=\"https://colab.research.google.com/github/iFallenHunt/nota/blob/main/calculo_de_media.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "SYv8NXrjuryQ"
      },
      "outputs": [],
      "source": [
        "m1 = float(input('Digite a nota M1: '))\n",
        "m2 = float(input('Digite a nota M2: '))\n",
        "m3 = float(input('Digite a nota M3: '))\n",
        "\n",
        "media = (m1 + m2 + m3) / 3 \n",
        "\n",
        "if media >= 0.0 and media <= 4.0:\n",
        "  print('Aluno reprovado')\n",
        "elif media >= 4.1 and media <= 6.0:\n",
        "  exame = float(input('Digite a nota do exame'))\n",
        "  if exame >= 6.0:\n",
        "    print('Aprovado no exame')\n",
        "  else:\n",
        "    print('Reprovado no exame') \n",
        "else:\n",
        "  print('Aluno aprovado')    "
      ]
    }
  ]
}