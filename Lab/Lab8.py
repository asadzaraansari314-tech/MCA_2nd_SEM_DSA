{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9364b657",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Queue: [23]\n",
      "Queue: [23, 45]\n",
      "Removed: 23\n",
      "Queue: [45]\n"
     ]
    }
   ],
   "source": [
    "queue = []\n",
    "\n",
    "def enqueue():\n",
    "    val = int(input(\"Enter value: \"))\n",
    "    queue.append(val)\n",
    "    print(\"Queue:\", queue)\n",
    "\n",
    "def dequeue():\n",
    "    if len(queue) == 0:\n",
    "        print(\"Queue is empty\")\n",
    "    else:\n",
    "        print(\"Removed:\", queue.pop(0))\n",
    "        print(\"Queue:\", queue)\n",
    "\n",
    "enqueue()\n",
    "enqueue()\n",
    "dequeue()"
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
