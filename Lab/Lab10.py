{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8c45acee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Row Major Order:\n",
      "1 2 3 4 5 6 7 8 9 "
     ]
    }
   ],
   "source": [
    "matrix = [[1, 2, 3],\n",
    "          [4, 5, 6],\n",
    "          [7, 8, 9]]\n",
    "\n",
    "print(\"Row Major Order:\")\n",
    "for row in matrix:\n",
    "    for val in row:\n",
    "        print(val, end=\" \")"
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
