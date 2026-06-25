{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8a63b91",
   "metadata": {},
   "outputs": [],
   "source": [
    "matrix = [[1, 2, 3],\n",
    "          [4, 5, 6],\n",
    "          [7, 8, 9]]\n",
    "\n",
    "print(\"Column Major Order:\")\n",
    "for i in range(len(matrix[0])):\n",
    "    for j in range(len(matrix)):\n",
    "        print(matrix[j][i], end=\" \")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
