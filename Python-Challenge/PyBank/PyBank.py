{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os \n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [],
   "source": [
    "csvpath = \"/Users/basy/Desktop/homework/Python-Challenge/PyBank/Resources/budget_data.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_to_load = os.path.join(\"Resources\", \"budget_data.csv\")\n",
    "file_to_output = os.path.join(\"analysis\", \"budget_analysis.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(csvpath) as budgeting_data:\n",
    "    reader = csv.reader(csvpath)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_to_output = (\"budget_data.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {},
   "outputs": [],
   "source": [
    "# List to store data\n",
    "total_months = 0\n",
    "month_of_change = []\n",
    "net_change_list = []\n",
    "greatest_increase = [\"\", 0]\n",
    "greatest_decrease = [\"\", 9999999]\n",
    "total_net = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CSV Header: ['/']\n"
     ]
    }
   ],
   "source": [
    "csv_header = next(reader)\n",
    "print(f\"CSV Header: {csv_header}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['U']\n"
     ]
    }
   ],
   "source": [
    "first_row = next(reader)\n",
    "print(first_row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_csv.reader object at 0x7fee69cebba0>\n"
     ]
    }
   ],
   "source": [
    "print(reader)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['s']\n",
      "['e']\n",
      "['r']\n",
      "['s']\n",
      "['/']\n",
      "['b']\n",
      "['a']\n",
      "['s']\n",
      "['y']\n",
      "['/']\n",
      "['D']\n",
      "['e']\n",
      "['s']\n",
      "['k']\n",
      "['t']\n",
      "['o']\n",
      "['p']\n",
      "['/']\n",
      "['h']\n",
      "['o']\n",
      "['m']\n",
      "['e']\n",
      "['w']\n",
      "['o']\n",
      "['r']\n",
      "['k']\n",
      "['/']\n",
      "['P']\n",
      "['y']\n",
      "['t']\n",
      "['h']\n",
      "['o']\n",
      "['n']\n",
      "['-']\n",
      "['C']\n",
      "['h']\n",
      "['a']\n",
      "['l']\n",
      "['l']\n",
      "['e']\n",
      "['n']\n",
      "['g']\n",
      "['e']\n",
      "['/']\n",
      "['P']\n",
      "['y']\n",
      "['B']\n",
      "['a']\n",
      "['n']\n",
      "['k']\n",
      "['/']\n",
      "['R']\n",
      "['e']\n",
      "['s']\n",
      "['o']\n",
      "['u']\n",
      "['r']\n",
      "['c']\n",
      "['e']\n",
      "['s']\n",
      "['/']\n",
      "['b']\n",
      "['u']\n",
      "['d']\n",
      "['g']\n",
      "['e']\n",
      "['t']\n",
      "['_']\n",
      "['d']\n",
      "['a']\n",
      "['t']\n",
      "['a']\n",
      "['.']\n",
      "['c']\n",
      "['s']\n",
      "['v']\n"
     ]
    }
   ],
   "source": [
    "for row in reader:\n",
    "    print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "total_months += 1\n",
    "print(total_months)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "()\n"
     ]
    }
   ],
   "source": [
    "output = ()\n",
    "print (output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
