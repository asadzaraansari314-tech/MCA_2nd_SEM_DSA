{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8da0d4da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 -> 20 -> 30 -> 11\n"
     ]
    }
   ],
   "source": [
    "class Node:\n",
    "    def __init__(self, data):\n",
    "        self.data = data\n",
    "        self.next = None\n",
    "\n",
    "class LinkedList:\n",
    "    def __init__(self):\n",
    "        self.head = None\n",
    "\n",
    "    def insert(self, data):\n",
    "        new_node = Node(data)\n",
    "        if not self.head:\n",
    "            self.head = new_node\n",
    "            return\n",
    "        temp = self.head\n",
    "        while temp.next:\n",
    "            temp = temp.next\n",
    "        temp.next = new_node\n",
    "\n",
    "    def display(self):\n",
    "        temp = self.head\n",
    "        while temp:\n",
    "            print(temp.data, end=\" -> \")\n",
    "            temp = temp.next\n",
    "\n",
    "ll = LinkedList()\n",
    "ll.insert(10)\n",
    "ll.insert(20)\n",
    "ll.insert(30)\n",
    "ll.display()\n"
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
