class Jar:
    def __init__(self, capacity=12):
        if isinstance(capacity, str):
            try:
                int(capacity)
            except:
                raise ValueError()
        elif not capacity:
            raise ValueError()
        elif capacity > 0:
            self._capacity = capacity
            self._size = 0
        else:
            raise ValueError()

    def __str__(self):
        n = self._size
        cookie = "🍪"
        return (cookie*n)


    def deposit(self, n):
        if self._capacity >= (self._size + n) and n >= 0:
            self._size += n
        else:
            raise ValueError()
        return self._size

    def withdraw(self, n):
        if (self._size - n) >= 0 and n >= 0:
            self._size -= n
        else:
            raise ValueError()
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    Jar1 = get_jar()
    Jar1.deposit(int(input("deposit: ")))
    Jar1.withdraw(int(input("withdraw: ")))
    print(Jar1)

def get_jar():
    cap = input("capacity: ")
    return Jar(cap)


if __name__ == "__main__":
    main()
