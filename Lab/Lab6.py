{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "746e3767",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "41\n"
     ]
    }
   ],
   "source": [
    " \n",
    "def evaluate_expression(expression):\n",
    "    stack = []\n",
    "    for char in expression.split():\n",
    "        if char.isdigit():\n",
    "            stack.append(int(char))\n",
    "        else:\n",
    "            b = stack.pop()\n",
    "            a = stack.pop()\n",
    "        if char ==\"+\":\n",
    "            stack.append(a+b)\n",
    "        elif char ==\"-\":\n",
    "            stack.append(a-b)\n",
    "        elif char ==\"*\":\n",
    "            stack.append(a*b)\n",
    "        elif char ==\"/\":\n",
    "            stack .append(a/b)\n",
    "    return stack[0]\n",
    "exp= \"6 5  * 5 4 * + 9 -\"\n",
    "print(evaluate_expression(exp))            \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "430fc487",
   "metadata": {},
   "outputs": [],
   "source": []
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
