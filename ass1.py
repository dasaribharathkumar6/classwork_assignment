#!/usr/bin/env python
# coding: utf-8

# In[14]:


a = "Hello"
print(a)


# In[15]:


a = "Hello, World!"
print(a[1])


# In[16]:


b = "Hello, World!"
print(b[2:5])


# In[17]:


a = "Hello, World!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.replace("H", "J"))


# In[18]:


a = "Hello"
b = "World"
c = a + " " + b
print(c)


# In[20]:


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "66052c6b-7c33-4bd1-b8d6-b9165eb9adf7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n"
     ]
    }
   ],
   "source": [
    "a=\"hello\"\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5585dc5e-9c42-47fa-83a6-039f3b55ecd7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "e\n",
      "llo\n"
     ]
    }
   ],
   "source": [
    "a=\"hello, world!\"\n",
    "print(a[1])\n",
    "b=\"hello , world!\"\n",
    "print(b[2:5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e7f13480-c8de-4781-8f3c-6fc1ac50ab34",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13\n",
      "HELLO, WORLD!\n",
      "hello, world!\n",
      "jello, world!\n"
     ]
    }
   ],
   "source": [
    "a=\"hello, world!\"\n",
    "print(len(a))\n",
    "print(a.upper())\n",
    "print(a.lower())\n",
    "print(a.replace(\"h\",\"j\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "51b6df3b-e3a6-49c4-a106-588824885bab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "a=\"Hello\"\n",
    "b=\"World\"\n",
    "c= a + \" \" + b\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "13a9c6c5-2859-48fa-a263-328614dfce62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "h\n",
      "e\n",
      "l\n",
      "l\n",
      "o\n",
      " \n",
      "w\n",
      "o\n",
      "r\n",
      "l\n",
      "d\n"
     ]
    }
   ],
   "source": [
    "a=\"hello world\"\n",
    "for ch in a:\n",
    "    print(ch)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a49fdbf9-036a-41f2-a1f3-1c068075d171",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "given string: Ss\n",
      "concatenated string: Ss Brown\n"
     ]
    }
   ],
   "source": [
    "a=\"Ss\"\n",
    "print(\"given string:\", a)\n",
    "new_string = a + \" \" \"Brown\"\n",
    "print(\"concatenated string:\", new_string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "21cbc007-947f-4b47-999a-4aba9186fa37",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "given string: Hel\n",
      "string: Hello \n"
     ]
    }
   ],
   "source": [
    "#string slicing\n",
    "given_string = \"Hello World!\"\n",
    "substring= given_string[0:3]\n",
    "substring1=given_string[:6]\n",
    "print(\"given string:\", substring)\n",
    "print(\"string:\", substring1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "df7e6927-1f8f-492b-afa2-95b0d1ed19ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\"world\" is in \"hello world\"\n"
     ]
    }
   ],
   "source": [
    "#using in operator\n",
    "a=\"hello world\"\n",
    "b=\"world\"\n",
    "if b in a:\n",
    "    print(f'\"{b}\" is in \"{a}\"')\n",
    "else:\n",
    "      print(f'\"{b}\"is not in \"{a}\"')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ffd34493-e7be-43f0-bb25-ffa7c5d1efe0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['1', '2', '3', '4', '5']\n"
     ]
    }
   ],
   "source": [
    "my1='1/2/3/4/5'\n",
    "num=my1.split('/')\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "79c31cd8-7807-4960-ae14-a42bf7bf2b43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['peach col', ' is ', 'nage ', ' chocolate']\n"
     ]
    }
   ],
   "source": [
    "my2=\"peach color is ornage or chocolate\"\n",
    "num=my2.split('or')\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8238825d-737c-4316-8f1b-b5edea49b1d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['1', '2', '3', '4', '5']\n"
     ]
    }
   ],
   "source": [
    "my1='1%2%3%4%5'\n",
    "num=my1.split('%')\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "8824a0f0-9cdb-43c7-8400-f44b342f2c5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['peach color is orm or chocolate ', ' i hate choloate']\n"
     ]
    }
   ],
   "source": [
    "my2=\"peach color is orm or chocolate and i hate choloate\"\n",
    "num=my2.split('and')\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8f52dfbd-80c0-4386-8fb3-36ed8d64f42d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a=\"038\"\n",
    "x=a.isdigit()\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "859e8c8b-685f-4eab-b7af-18b5c33ffa5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a=\"bharath\"\n",
    "x=a.isalnum()\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a3d84621-63c8-4533-944c-5cd79318e88b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a=\"hello world\"\n",
    "x=a.is
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1afcb843-b09f-438b-ba2c-2ec81e489549",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a= \" \"\n",
    "x=a.isspace()\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3e7f2d6a-7ca5-4fc7-8599-68958ac9699c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "a=\"bharathkumar\"\n",
    "x=a.isupper()\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "123bdaeb-c5a2-4a64-a38f-d40edf0b8f6c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello bharath kumar\n",
      "\"Hello bharath\"\n",
      "\"Hello bharath\"\n",
      "\"Hello bharath\"\n"
     ]
    }
   ],
   "source": [
    "#string methods\n",
    "a=\"HELLO BHARATH KUMAR\"\n",
    "x=a.lower()\n",
    "print(x)\n",
    "\n",
    "#lstrip()\n",
    "\n",
    "a=\" Hello bharath \"\n",
    "x=a.strip()\n",
    "left_strip=a.lstrip()\n",
    "right_strip=x.rstrip()\n",
    "print(f'\"{x}\"')\n",
    "print(f'\"{left_strip}\"')\n",
    "print(f'\"{right_strip}\"')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4ca94cbe-1ab4-4694-8918-5b7b40ca8fd3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "x=\"hello bharath\"\n",
    "r1=x.endswith(\"bharath\")\n",
    "r2=x.endswith(\"bharath\")\n",
    "print(f'{r1}')\n",
    "print(f'{r2}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ab71732f-7994-4378-b911-215939d21c4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "-1\n",
      "Hello Prof. Nikshep, How are you\n"
     ]
    }
   ],
   "source": [
    "x=\"Hello bharath, How are you\"\n",
    "a=x.find(\"bharath\")\n",
    "b=x.find(\"world\")\n",
    "\n",
    "# replace substring\n",
    "given_string = x.replace(\"bharath\", \"Prof. Nikshep\")\n",
    "\n",
    "\n",
    "print(f'{a}')\n",
    "print(f'{b}')\n",
    "print(f'{given_string}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "30372a2f-873b-4224-817a-11e55da11621",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hellohellohellohello\n"
     ]
    }
   ],
   "source": [
    "#repetition operator \n",
    "x=\"hello\"\n",
    "y=x*4\n",
    "print(f'{y}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "62230751-9875-480a-b227-23055fa2678a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}


# In[ ]:
