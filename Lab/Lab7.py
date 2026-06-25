{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eaf234db",
   "metadata": {},
   "outputs": [],
   "source": [
    "def factorial(n):\n",
    "    if n == 0 or n == 1:\n",
    "        return 1\n",
    "    return n * factorial(n - 1)\n",
    "\n",
    "num = int(input(\"Enter number: \"))\n",
    "print(\"Factorial:\", factorial(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "969c3c85",
   "metadata": {},
   "outputs": [],
   "source": [
    "def factorial_stack(n):\n",
    "    if n < 0: return \"Error: Negative input\"\n",
    "    if n == 0 or n == 1: return 1\n",
    "    \n",
    "    stack = []\n",
    "    \n",
    "    # Phase 1: Winding (Pushing values onto the stack)\n",
    "    while n > 1:\n",
    "        stack.append(n)\n",
    "        n -= 1\n",
    "    \n",
    "    result = 1\n",
    "    \n",
    "    # Phase 2: Unwinding (Popping and multiplying)\n",
    "    while stack:\n",
    "        current_val = stack.pop()\n",
    "        result *= current_val\n",
    "        \n",
    "    return result\n",
    "\n",
    "# Example\n",
    "print(f\"5! is: {factorial_stack(5)}\") # Output: 120"
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
   "name": "python",
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
